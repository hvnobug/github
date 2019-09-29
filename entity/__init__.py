from mongoengine import connect

from entity.GithubUser import GithubUser
from entity.GithubRepository import GithubRepository
from util import mongo_url

connect(
    host=mongo_url
)
