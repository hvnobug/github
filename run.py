import time

import requests

from common import GithubUserRepository, GithubUser
from listener import RepoUpdateListener

username = 'hvnobug'

# 可以生成 用户相关 github api
gu = GithubUser(username)

# 监听器列表
listeners = []


def main():
    start_listen()


def start_listen():
    """
    监听仓库更新
    """
    # 获取用户 starred 仓库列表
    result = requests.get(gu.starred_url()).json()
    for repository in result:
        repo = repository['name']
        user = repository['owner']['login']
        # 可以生成 仓库相关 github api
        gur = GithubUserRepository(user, repo)
        time.sleep(10)
        # 监听仓库更新并发送邮件通知
        listener = RepoUpdateListener(github_repo=gur, duration=600)
        listeners.append(listener)
        listener.start()


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
