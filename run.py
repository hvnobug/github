import time
from common import GithubUserRepository, GithubUser
from listener import RepoUpdateListener

# 仓库所有者
user = 'spring-projects'
# 仓库名称
repo = 'spring-boot'

# 可以生成 仓库相关 github api
gur = GithubUserRepository(user, repo)
# 可以生成 用户相关 github api
gu = GithubUser(user)


def main():
    listen_repo_update()


def listen_repo_update():
    """
    监听仓库更新
    """
    # listener = RepoUpdateListener(user=user,repo=repo, duration=600)
    listener = RepoUpdateListener(github_repo=gur, duration=600)
    listener.start()


if __name__ == '__main__':
    main()
    while True:
        time.sleep(1)
