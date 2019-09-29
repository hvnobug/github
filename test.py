import math
from _datetime import datetime
from collections.abc import Iterable

import requests

from common import GithubRepositoryUrls, GithubUserUrls
from entity import GithubUser, GithubRepository
from util import print_table, ufc_datetime_format, format_ufc_datetime
from util.bean import get_object_attrs, object2dict
from util.mongo import mongo_collection


def test_mongo_collect1():
    with mongo_collection('github_repository') as github_repository:
        print_table(github_repository.find())


def test_mongo_collect2():
    print_table(GithubRepository.objects())


def test_mongo_orm():
    def save_user_repo():
        json = requests.get(GithubUserUrls('hvnobug').starred_url()).json()
        for item in json:
            node_id = item['node_id']
            name = item['name']
            forks = item['forks']
            fork = item['fork']
            private = item['private']
            watchers = item['watchers']
            language = item['language']
            full_name = item['full_name']
            owner = item['owner']['login']
            created_at = format_ufc_datetime(item['created_at'])
            updated_at = format_ufc_datetime(item['updated_at'])
            stars = item['stargazers_count']
            open_issues = item['open_issues']
            gr = GithubRepository(
                owner=owner, name=name, stars=stars, forks=forks, private=private, watchers=watchers,
                language=language, full_name=full_name, open_issues=open_issues, fork=fork,
                created_at=created_at, updated_at=updated_at, id=item['id'], node_id=node_id)
            gr.create_time = datetime.now()
            gr.save()

    save_user_repo()
    print_table(GithubRepository.objects.all())


test_mongo_collect2()
