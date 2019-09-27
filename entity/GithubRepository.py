from mongoengine import StringField, DateTimeField, LongField, Document, BooleanField, ObjectIdField, queryset_manager


class GithubRepository(Document):
    id = LongField(primary_key=True)
    node_id = StringField()
    owner = StringField(required=True)
    name = StringField(required=True)
    full_name = StringField(required=True)
    create_time = DateTimeField()
    update_time = DateTimeField()
    created_at = DateTimeField()
    updated_at = DateTimeField()
    stars = LongField(default=0)
    forks = LongField(default=0)
    fork = BooleanField()
    watchers = LongField(default=0)
    open_issues = LongField(default=0)
    private = BooleanField()
    language = StringField(required=False)

    @queryset_manager
    def objects(cls, query_set):
        # This may actually also be done by defining a default ordering for
        # the document, but this illustrates the use of manager methods
        return query_set.order_by('-stars', '-forks', '-watchers')
