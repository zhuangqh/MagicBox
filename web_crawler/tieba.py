# -*- coding: utf-8 -*-
import string
import urllib2


def baidu_tieba(url, begin_page, end_page):
    for i in range(begin_page, end_page):
        sName = string.zfill(i, 5) + '.html'
        print '正在下载' + str(i) + '个网页，并将其存储为' + sName + '....'
        f = open(sName, 'w+')
        m = urllib2.urlopen(url + str(i)).read()
        f.write(m)
        f.close()


bdurl = str(raw_input(u'input url\n'))
begin_page = int(raw_input(u'start page\n'))
end_page = int(raw_input(u'end page\n'))

baidu_tieba(bdurl, begin_page, end_page)
