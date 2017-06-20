#/bin/bash
# coding: utf-8

import os
import re
import urllib
import sys
import chardet
import traceback
from BeautifulSoup import BeautifulSoup 
import requests
from lxml import etree
from twilio.rest import Client
import time
import traceback

realpath = os.path.split(os.path.realpath(__file__))[0]

def	sedMessage(mybody):
	account_sid = "AC06f36b0202ae459eaec8d2ff746debf9"
	auth_token	= "3a437340445793f34850f87e70a09cdf"
	client = Client(account_sid, auth_token)

	message = client.messages.create(
		to="+8618810559580", 
		from_="+12342310358",
		body=mybody)
	message.sid
	#print(message.sid)

def getRequests(url):
	r = requests.get(url)
	content = r.text
	selector = etree.HTML(content.encode('latin1','ingore'))
	return selector

def	getInfo(url,data_in):
	prefix_url = '/'.join(url.split('/')[:-1])
	selector = getRequests(url)
	titles = selector.xpath('//ul/li/a/@title')
	links = selector.xpath('//ul/li/a[@title]/@href')
	for i,each in enumerate(titles):
		info = '%s\t%s/%s\n' % (each.strip(), prefix_url,links[i])
		if info.encode('utf8','ignore') not in data_in:
			file = '%s/data/data.info' % (realpath)
			data_out = open(file,'ab')
			data_out.write(info.encode('utf8','ignore'))
			sedMessage(info)
			data_out.close()

def	getInfo2(url,data_in):
	selector = getRequests(url)
	titles = selector.xpath('//div[@class="c_rr02box_list"]/ul[@class="list fixed"]/li/a/@title')
	links = selector.xpath('//div[@class="c_rr02box_list"]/ul[@class="list fixed"]/li/a/@href')
	for i ,each in enumerate(titles):
		info = '%s\t%s/%s\n' % (each.strip(),url,links[i])
		if info.encode('utf8','ignore') not in data_in:
			file = '%s/data/data.info' % (realpath)
			data_out = open(file,'ab')
			data_out.write(info.encode('utf8','ignore'))
			print info.encode('utf8','ignore')
			#sedMessage(info)
			data_out.close()

def	run():
	file = '%s/data/data.info' % (realpath)
	data_in = open(file,'rb').readlines()
	#anounceInfo = 'http://yjs.cueb.edu.cn/xwgg/ggtz/index.htm'
	#recruitInfo = 'http://yjs.cueb.edu.cn/zsks/zsdt/index.htm'
	#getInfo(anounceInfo,data_in)
	#getInfo(recruitInfo,data_in)
	
	academic_trends = 'http://www.cueb.edu.cn/'
	getInfo2(academic_trends,data_in)

if	__name__=='__main__':
	f_log = open('%s/data/log.info' % realpath,'ab')

	run()
