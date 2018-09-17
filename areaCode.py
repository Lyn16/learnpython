#!/usr/bin/env python
import re
phone = "602-343-8747"
a = re.findall('^(.*?)-', phone)
print "The area code is:" + a[0]










