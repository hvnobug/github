import time

import requests

from common import GithubRepositoryUrls, GithubUserUrls
from listener import RepoUpdateListener
from util import logger

username = 'hvnobug'

# 可以生成 用户相关 github api
gu = GithubUserUrls(username)

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
    if isinstance(result, dict):
        message = result['message']
        logger.error(message)
        return
    for repository in result:
        repo = repository['name']
        user = repository['owner']['login']
        # 可以生成 仓库相关 github api
        gur = GithubRepositoryUrls(user, repo)
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
