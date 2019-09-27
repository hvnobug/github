> Python3.6

## 1. 依赖第三方库
> `zhon`(中文标点符号处理),`colorama`(在控制台、命令行输出彩色文字的模块),`prettytable`(来生成美观的 ASCII 格式的表格),`requests`(常用的 http 请求的模块),`APScheduler`(定时任务框架),`mongoengine`(Mongodb 的对象文档映射器)

```
pip install zhon
pip install colorama
pip install requests
pip install prettytable
pip install APScheduler
pip install mongoengine
```

## 2. 修改配置

### 2.1 修改邮箱配置

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

### 2.2 修改 mongo 配置
```python
mongo = {
    'host': '127.0.0.1',
    'port': 27017,
    'database': 'github',
    'username': None,
    'password': None
}
```

## 3. 监听仓库

> 修改 run.py 文件监听仓库更新

```python
import time
from common import GithubRepositoryUrls, GithubUserUrls
from listener import RepoUpdateListener

# 仓库所有者
user = 'spring-projects'
# 仓库名称
repo = 'spring-boot'

# 可以生成 仓库相关 github api
# gru = GithubRepositoryUrls(user, repo)
# 可以生成 用户相关 github api
# guu = GithubUserUrls(user)


def main():
    """
    监听仓库更新
    """
    listener = RepoUpdateListener(user=user,repo=repo, duration=600)
    # listener = RepoUpdateListener(github_repo=gru, duration=600)
    listener.start()


if __name__ == '__main__':
    main()
    while True:
        time.sleep(1)

```