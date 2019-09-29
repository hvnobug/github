from datetime import datetime

import requests

from entity import GithubRepository
from util import email, format_ufc_datetime
from util import logger
from abc import abstractmethod
from common import GithubRepositoryUrls
from apscheduler.schedulers.background import BackgroundScheduler


class Listener:
    def __init__(self, **kwargs):
        super().__init__()
        self.duration = kwargs.get('duration', 600)
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
        <center>
            <h1>Github仓库更新通知</h1>
        </center>
        <h3>
            您关注的仓库
            <a style="color:#DC143C;margin:0 10px;" href="{repo_url}">{repo_name}</a>已经更新
        </h3>
        """.format(repo_name=args[0], repo_url=args[1])
        email.send_emil('Github仓库更新通知', html, 'html')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        github_repo = kwargs.get('github_repo', None)
        if github_repo is None:
            self.__user = kwargs.get('user', None)
            self.__repo = kwargs.get('repo', None)
            self.__github_repo = GithubRepositoryUrls(self.__user, self.__repo)
        else:
            assert isinstance(github_repo, GithubRepositoryUrls), 'github_repo 必须是 GithubUserRepository 类型'
            self.__github_repo = github_repo
            self.__user = github_repo.user
            self.__repo = github_repo.repo
        self.listen()

    def listen(self):

        api_url = self.__github_repo.api_url()
        home_url = self.__github_repo.home_url()
        result = requests.get(api_url).json()
        message = result.get('message', None)
        if message:
            logger.error(message)
            return
        gr_id = result['id']
        created_at = format_ufc_datetime(result['created_at'])
        updated_at = format_ufc_datetime(result['updated_at'])
        full_name = result['full_name']

        def save_user_repo(repo):
            gr = GithubRepository(owner=repo['owner']['login'], name=repo['name'], stars=repo['stargazers_count'],
                                  forks=repo['forks'], private=repo['private'], watchers=repo['watchers'],
                                  language=repo['language'], full_name=full_name,
                                  open_issues=repo['open_issues'], fork=repo['fork'], created_at=created_at,
                                  updated_at=updated_at, id=gr_id, node_id=repo['node_id'])
            gr.create_time = datetime.now()
            gr.save()

        cur_gr = GithubRepository.objects(id=gr_id).first()
        if cur_gr:
            cur_updated_at = cur_gr.updated_at
            if updated_at > cur_updated_at:
                logger.info('{repo_name} 已更新'.format(repo_name=full_name))
                self.notify(full_name, home_url)
            else:
                logger.info('{repo_name} 未更新'.format(repo_name=full_name))
        save_user_repo(result)

    def start(self):
        logger.info('正在监听仓库 - {user}/{repo} 更新'.format(user=self.__user, repo=self.__repo))
        super().start()

    def shutdown(self):
        super().shutdown()

    def pause(self):
        super().pause()
