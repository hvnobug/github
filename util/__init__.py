from urllib import parse

from common import mongo_config as config
from util.color import color
from util.datetime import simple_datetime_format, ufc_datetime_format, format_ufc_datetime
from util.banner import print_banner
from util.bean import get_object_attrs, object2dict
from util.language import is_contain_chinese, is_chinese, str_count, str_zh_count, str_zh_and_pu_count
from util.logger import logger
from util.mail import email
from util.print_table import print_table

host = config['host']
port = config['port']
username = config['username']
password = parse.quote_plus(config['password'])
db = config['database']
auth = config['auth']
auth_database = config['auth_database']
auth_mechanism = config['auth_mechanism']
mongo_url = 'mongodb://{0}:{1}@{2}:{3}/{4}?authSource={5}&authMechanism={6}'.format(
    username, password, host, port, db, auth_database, auth_mechanism) \
    if auth else 'mongodb://{0}@{1}/{2}'.format(host, port, db)
print_banner()
