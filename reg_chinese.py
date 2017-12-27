#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re;

str=u"<title>心理箴言</title>"

# pattern =re.compile(u'[\u4e00-\u9fa5]')
#pattern =re.compile(u"[\u4e00-\u9fa5]+")
pattern =re.compile(u"<title>.*?<")
result=re.findall(pattern,str)
# print result.group()
for w in result:
    print w
