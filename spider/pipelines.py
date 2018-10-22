# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from google.cloud import firestore
from google.oauth2 import service_account
import json

class SpiderPipeline(object):
    def process_item(self, item, spider):
        return item

class FirestorePipeline(object):

    collection_name = 'products'

    def __init__(self, creds):
        self.creds = creds

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            creds=json.loads(crawler.settings.get('FIREBASE')),
        )

    def open_spider(self, spider):
        # print (self.creds)
        credentials = service_account.Credentials.from_service_account_info(info=self.creds)
        print credentials
        self.db = firestore.Client(project='modum-e2bbb', credentials=credentials)
        # pymongo.MongoClient(self.mongo_uri)
        # self.db = self.client[self.mongo_db]

    # def close_spider(self, spider):
        # self.client.close()

    def process_item(self, item, spider):
        product = dict(item)
        docRef = self.db.collection(self.collection_name).document(product['store']+'_'+product['sku'])
        docRef.set(product)
        # self.db[self.collection_name].document(dict(item))
        return item