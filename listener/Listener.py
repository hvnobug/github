from abc import abstractmethod
from apscheduler.schedulers.background import BackgroundScheduler
import requests

from common import GithubUserRepository
from service import email
from util import logger

logger.name = __name__


class Listener:
    def __init__(self, **kwargs):
        super().__init__()
        self.duration = kwargs.get('duration', 600)
        self.cur_update = None
        self.last_update = None
        self.scheduler = BackgroundScheduler()
        self.scheduler.add_job(self.listen, 'interval', seconds=self.duration)

    @abstractmethod
    def listen(self):
        """
        开始监听
        """
        pass

    def start(self):
        self.scheduler.start()

    def notify(self, *args, **kwargs):
        pass

    def shutdown(self):
        self.scheduler.shutdown()

    def pause(self):
        self.scheduler.pause()


class RepoUpdateListener(Listener):

    def notify(self, *args, **kwargs):
        html = """
        <center><h2>Github仓库更新通知</h2></center>
        <p>您关注的仓库<span style="color='red'">{repo_name}</span>已经更新</p>
        <p>请点击<a href="{repo_url}">链接</a>查看</p>
        """.format(repo_name=args[0], repo_url=args[1])
        email.send_emil('Github仓库更新通知', html, 'html')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        github_repo = kwargs.get('github_repo', None)
        if github_repo is None:
            self.__user = kwargs.get('user', None)
            self.__repo = kwargs.get('repo', None)
            self.__github_repo = GithubUserRepository(self.__user, self.__repo)
        else:
            assert isinstance(github_repo, GithubUserRepository), 'github_repo must instance of GithubUserRepository'
            self.__github_repo = github_repo
            self.__user = github_repo.user
            self.__repo = github_repo.repo

    def listen(self):
        api_url = self.__github_repo.api_url()
        home_url = self.__github_repo.home_url()
        result = requests.get(api_url).json()
        self.last_update = result['updated_at']
        if not self.cur_update:
            self.cur_update = self.last_update
        full_name = result['full_name']
        if self.last_update < self.cur_update:
            self.last_update = self.cur_update
            logger.info('{repo_name} 已更新'.format(repo_name=full_name))
            self.notify(full_name, home_url)
        else:
            logger.info('{repo_name} 未更新'.format(repo_name=full_name))

    def start(self):
        logger.info('正在监听仓库 - {user}/{repo} 更新'.format(user=self.__user, repo=self.__repo))
        super().start()

    def shutdown(self):
        super().shutdown()

    def pause(self):
        super().pause()
