import time

import requests

from common import GithubUserRepository, GithubUser
from listener import RepoUpdateListener

username = 'hvnobug'

# 可以生成 仓库相关 github api
# 可以生成 用户相关 github api
gu = GithubUser(username)

listeners = []


def main():
    start_listen()


def start_listen():
    """
    监听仓库更新
    """
    result = requests.get(gu.starred_url()).json()
    for repository in result:
        repo = repository['name']
        user = repository['owner']['login']
        gur = GithubUserRepository(user, repo)
        time.sleep(10)
        listener = RepoUpdateListener(github_repo=gur, duration=600)
        listener.start()
        listeners.append(listener)


def pause_listen():
    """
    暂停监听
    """
    for listener in listeners:
        listener.pause()


def stop_listen():
    """
    停止监听
    """
    for listener in listeners:
        listener.shutdown()


if __name__ == '__main__':
    main()
    while True:
        time.sleep(1)
