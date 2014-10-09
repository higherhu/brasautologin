#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 30 11:07:29 2014

@author: Higher
@Email: hujiagao@gmail.com
"""

import urllib
import urllib2
import json
import time
import random

import sys
reload(sys)
sys.setdefaultencoding('utf8')

username = ''
password = ''


def getTime():
    return time.strftime("%Y-%m-%d %H:%M:%S\t")


def login():
    url = 'http://p.nju.edu.cn/portal/portal_io.do'
    values = {'action': 'login',
              'username': username,
              'password': password}
    data = urllib.urlencode(values)

    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)
    the_page = response.read()
    retJson = json.loads(the_page)

    msg = getTime() + retJson['reply_message']
    print msg

    return retJson


def getAcctsessionid():
    url = 'http://p.nju.edu.cn/proxy/onlinelist.php'
    values = {'username': username,
              'password': password}
    data = urllib.urlencode(values)

    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)
    the_page = response.read()
    retJson = json.loads(the_page)

    try:
        asid = str(retJson['online'][0]['acctsessionid'])
    except: #未登录，则无法获取acctsessionid
        asid = None

    return asid


def logout(acctsessionid):
    url = 'http://p.nju.edu.cn/proxy/disconnect.php'

    values = {'acctsessionid': acctsessionid,
              'username': username,
              'password': password}

    data = urllib.urlencode(values)

    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)
    the_page = response.read()
    retJson = json.loads(the_page)

    msg = getTime() + str('logout:') + retJson['reply_msg']
    print msg

    return retJson


def onInternet(tout=3, url='http://www.baidu.com'):
    try:
        req = urllib2.Request(url)
        response = urllib2.urlopen(req, timeout=tout)
    except:
        return False

    return True


if __name__=='__main__':
    while True:
        if not onInternet():
            msg = getTime() + u'无法访问互联网!尝试登录Bras...'
            print msg

            acctsessionid = getAcctsessionid()
            if acctsessionid:
                msg = getTime() + u'远端下线...'
                print msg

            login()
        else:
            msg = getTime() + u'可以访问互联网!'
            print msg

        waitTime = random.randint(5,15)
        msg = getTime() + str(waitTime) + u'分钟后执行下次检测。'
        print msg
        time.sleep(60*waitTime)

