#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""  TODO: module description

Usage:  

Input:  

Output:  

Author: wenhai.pan

Create Time:    2019-08-23 11:59:25

"""

import sys
import os
import time
from datetime import datetime, timedelta

import scrapy

class BaoSpider(scrapy.Spider):
    name = "bao"
    start_urls = [
            'http://m.27bao.com/gif'
    ]

    def parse(self, response):

        gifset_url_list = response.css("li p.p_title a::attr(href)").getall()

        for gifset_url in gifset_url_list:
            yield response.follow(gifset_url, self.parse_gifset)

        #print(gifset_url_list)

        try:
            next_url = response.css("div.page a.a1::attr(href)").getall()[-2]
            #print(next_url)
            yield response.follow(gifset_url, self.parse)
        except:
            return

        return


    def parse_gifset(self, response):

        try:
            title = response.css("html body article#content h1::text").getall()[0]
            gif_url = response.css("article img::attr(src)").getall()[0]
            next_url = response.css("div#pages a.a1::attr(href)").getall()[-1]

            yield {
                "title": title,
                "file_urls": [gif_url]
            }

            #print(title)
            #print(gif_url)
            #print(next_url)

            yield response.follow(next_url, self.parse_gifset)

        except:
            return



def main():
    return

if __name__ == "__main__":
    main()


