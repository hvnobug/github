from mongoengine import StringField, DateTimeField, LongField, Document


class GithubUser(Document):
    user = StringField(required=True)
    create_time = DateTimeField()
    update_time = DateTimeField()
    following = LongField(default=0)
    follower = LongField(default=0)
