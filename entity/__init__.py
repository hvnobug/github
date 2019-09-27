from mongoengine import connect
from common import mongo_config as config

from entity.GithubUser import GithubUser
from entity.GithubRepository import GithubRepository

connect(
    host=config['host'],
    port=config['port'],
    db=config['database'],
    username=config['username'],
    password=config['password']
)
