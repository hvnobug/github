## 修改配置

> 修改邮箱相关配置,默认使用 qq 邮箱,修改 common/config.py
```python
email = {
    'sender': ['your email', 'your name'],
    'secure': 'your secure',
     # qq 邮箱服务器,使用其他邮箱请修改服务器端口
    'host': 'smtp.qq.com',
    'receivers': [
        ['receiver`s email', 'receiver`s name']
    ],
    'user_ssl': True,
    'port': 25,
    'ssl_port': 465,
    'charset': 'utf-8'
}
```

## 监听仓库

> 修改 run.py 文件监听仓库更新

```python
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

```