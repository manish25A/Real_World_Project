from __future__ import absolute_import
from django.conf import settings
from redis import Redis as RedisBase
from enuff.utils import ensure_pk

class Redis(RedisBase):
    def __init__(self, **kwargs):
        kwargs = kwargs or {}
        if not 'port' in kwargs:
            kwargs['port'] = settings.REDIS_PORT
        if not 'host' in kwargs:
            kwargs['host'] = settings.REDIS_HOST
        if not 'db' in kwargs:
            kwargs['db'] = settings.REDIS_DB
        super(Redis,self).__init__(**kwargs)

class RedisBackend(object):
    def __init__(self, conn=None):
        self.conn = conn or Redis()

    def get_queue_template(self):
        raise NotImplementedError

    def remove(self, queue, instance):
        self.conn.lrem(queue, ensure_pk(instance))

    def add(self, queue, instance):
        self.conn.lpush(queue, ensure_pk(instance))

    def trim(self, queue, trim):
        self.conn.ltrim(queue, 0, trim)

    def get_ids(self, queue, limit=None):
        return map(int, self.conn.lrange(queue, 0, limit or -1))
