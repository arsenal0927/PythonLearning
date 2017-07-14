# !/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf8')

from suds.client import Client
from suds.transport.https import HttpAuthenticated

url = 'http://172.20.40.7/Integration/Sync/Service/GetAllVideo.asmx?wsdl'

client = Client(url)

print client

print client.service.AllVideo(name = '网球比赛')