# -*- coding: utf-8 -*-


import pymongo
from doubanTop250.settings import MONGODB_HOST, MONGODB_NAME, MONGODB_PORT


class DoubanMovieTop250Pipeline(object):
    def __init__(self):
        client = pymongo.MongoClient(MONGODB_HOST, MONGODB_PORT)
        db = client[MONGODB_NAME]
        self.post = db['MovieTop250']

    def process_item(self, item, spider):
        data = dict(item)
        self.post.insert(data)
        return item


class DoubanMusicTop250Pipeline(object):
    def __init__(self):
        client = pymongo.MongoClient(MONGODB_HOST, MONGODB_PORT)
        db = client[MONGODB_NAME]
        self.post = db['MusicTop250']

    def process_item(self, item, spider):
        data = dict(item)
        self.post.insert(data)
        return item
