github_host = 'https://github.com'

github_api_host = 'https://api.github.com'


# 去除url结尾的'/'
def format_url(url: str): return format_url(url[:-1]) if url.endswith('/') else url


class GithubRepositoryUrls(object):

    def __init__(self, user: str, repo: str):
        assert user is not None, '参数 user 不能为 None'
        assert repo is not None, '参数 repo 不能为 None'
        self.__user = user
        self.__repo = repo

    @property
    def user(self):
        return self.__user

    @user.setter
    def user(self, user):
        self.__user = user

    @property
    def repo(self):
        return self.__repo

    @repo.setter
    def repo(self, repo):
        self.__repo = repo

    def home_url(self):
        """
        用户仓库主页
        """
        return format_url('{host}/{user}/{repo}'.format(host=github_host, user=self.__user, repo=self.__repo))

    def api_url(self):
        """
        用户仓库
        """
        return '{host}/repos/{user}/{repo}'.format(host=github_api_host, user=self.__user, repo=self.__repo)

    def fork_url(self):
        """
        仓库 fork
        """
        return '{repo_url}/forks'.format(repo_url=self.api_url())

    def teams_url(self):
        """
        仓库 teams
        """
        return '{repo_url}/teams'.format(repo_url=self.api_url())

    def hooks_url(self):
        """
        仓库 hooks
        """
        return '{repo_url}/hooks'.format(repo_url=self.api_url())

    def tags_url(self):
        """
        仓库 tags
        """
        return '{repo_url}/tags'.format(repo_url=self.api_url())

    def deployments_url(self):
        """
        仓库 deployments
        """
        return '{repo_url}/deployments'.format(repo_url=self.api_url())

    def issues_url(self, number):
        """
        仓库 issues
        """
        return format_url('{repo_url}/issues/{number}'.format(repo_url=self.api_url(), number=number))

    def pulls_url(self, number):
        """
        仓库 pulls
        """
        return format_url('{repo_url}/pulls/{number}'.format(repo_url=self.api_url(), number=number))

    def milestones_url(self, number):
        """
        仓库 milestones
        """
        return format_url('{repo_url}/milestones/{number}'.format(repo_url=self.api_url(), number=number))

    def labels_url(self, name):
        """
        仓库 labels
        """
        return format_url('{repo_url}/labels/{name}'.format(repo_url=self.api_url(), name=name))

    def releases_url(self, release_id):
        """
        仓库 releases
        """
        return format_url('{repo_url}/releases/{id}'.format(repo_url=self.api_url(), id=release_id))


class GithubUserUrls(object):
    def __init__(self, user: str):
        assert user is not None, '参数 user 不能为 None'
        self.__user = user

    def home_url(self):
        """
        用户主页
        """
        return format_url('{host}/{user}'.format(host=github_host, user=self.__user))

    def api_url(self):
        """
        api 接口的 url
        """
        return '{host}/users/{user}'.format(host=github_api_host, user=self.__user)

    def repos_url(self):
        """
        用户仓库
        """
        return '{api_url}/repos'.format(api_url=self.api_url())

    def followers_url(self):
        """
        用户粉丝
        """
        return '{api_url}/followers'.format(api_url=self.api_url())

    def following_url(self, other_user=''):
        """
        用户关注
        """
        return format_url('{api_url}/following/{other_user}'.format(api_url=self.api_url(), other_user=other_user))

    def gists_url(self, gist_id=''):
        """
        用户的 gists
        """
        return format_url('{api_url}/gists/{gist_id}'.format(api_url=self.api_url(), gist_id=gist_id))

    def starred_url(self, owner='', repo=''):
        """
        用户关注的仓库
        """
        return format_url('{api_url}/starred/{owner}/{repo}'.format(api_url=self.api_url(), owner=owner, repo=repo))

    def subscriptions_url(self):
        """
        用户订阅
        """
        return '{api_url}/subscriptions'.format(api_url=self.api_url())

    def organizations_url(self):
        """
        用户机构
        """
        return '{api_url}/orgs'.format(api_url=self.api_url())

    def events_url(self, privacy=''):
        """
        用户事件
        """
        return format_url('{api_url}/events/{privacy}'.format(api_url=self.api_url(), privacy=privacy))

    def received_events_url(self):
        """
        收到事件
        """
        return '{api_url}/received_events'.format(api_url=self.api_url())
