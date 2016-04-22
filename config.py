#!/usr/bin/env python
# coding:utf8

# 是否关闭log
debug_on = True

# 主循环 休眠时间
MAIN_LOOP_SLEEP_TIME = 6

# runspider 线程池
SPIDER_MAX_POOL_NUM = 3

# 运行多少次 runspider 后同步数据
RUN_SYNC_INTERVAL_TIMES = 5

# 运行多久 runspider 后同步数据
RUN_SYNC_INTERVAL_TIME = 20

# 一次同步多少条数据
SYNC_RECORDS_NUMS = 1000

# referer
REFERER = 'http://www.google.com'

# http通信密钥
ENCRYPT_MD5_KEY = '9b4fc52bc7208cd618195abee8d57ad6'

# 单个spider 初始化start_urls数目
MAX_START_URLS_NUM = 1

# request_domain = 'http://www.babel.com';
request_domain = 'http://www.tobabel.cn';

# 判断url是否重复
requst_distinct_url = request_domain+'/api/cluster-requst-distinct/index'

# 判断队列长度
requst_length_url = request_domain+'/api/get-spider-rules/get-length'

# 获取爬虫规则
request_url = request_domain+'/api/get-spider-rules/get'

# 同步last_md5 只是通用spider使用，rss不使用
sync_last_md5_url = request_domain+'/api/get-spider-rules/sync-last-md5'

# 同步爬取数据到线上数据库
sync_crawl_infos_url = request_domain+'/api/sync-crawl-infos/index'

# 数据库配置
db_host = '127.0.0.1'
db_user = 'root'
db_password = '123456'
db_name = 'babel'
db_table_name = 'bb_crawl_infos'
