"""
    Created by zgl on 18/5/15 23:40
"""

__author__ = 'zgl'


'''
http请求：
# urllib, requests
爬虫:
# scrapy, requests + beautiful soap
'''
import requests

class HTTP:
    @staticmethod
    def get(url, return_json=True):
        r = requests.get(url)

        if r.status_code !=200:
            return {} if return_json else ''
        return r.json() if return_json else r.text
