import time
from common import GithubUserRepository, GithubUser
from listener import RepoUpdateListener

user = 'spring-projects'
repo = 'spring-boot'

gur = GithubUserRepository(user, repo)
gu = GithubUser(user)


def main():
    listen_repo_update()


def listen_repo_update():
    listener = RepoUpdateListener(github_repo=gur, duration=600)
    listener.start()


def test():
    print('test')


if __name__ == '__main__':
    main()
    while True:
        time.sleep(1)
