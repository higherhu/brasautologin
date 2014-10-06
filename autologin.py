#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 30 11:07:29 2014

@author: Higher
@Email: hujiagao@gmail.com
"""

import urllib
import urllib2
import time
import json

username = ''    # 在引号内部填入学号
password = ''     # 在引号内部填入密码


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

    return the_page


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
    except:
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

    return the_page


if __name__ == '__main__':
    acctsessionid = getAcctsessionid()
    if acctsessionid:
        print u'远端下线...'
        logout(acctsessionid)

    print u'本机登录...'
    login()
