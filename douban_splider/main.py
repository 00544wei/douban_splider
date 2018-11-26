# __*__ coding: utf-8 __*__
from scrapy import cmdline

# cmdline.execute('scrapy crawl douban_splider -o douban.csv'.split())
cmdline.execute('scrapy crawl douban_splider'.split())