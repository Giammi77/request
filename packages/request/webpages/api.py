#!/usr/bin/python3
# -*- coding: utf-8 -*-
from gnr.core.gnrdecorator import public_method
import json
from datetime import datetime
import hashlib

# from gnr.web.gnrwebpage import GnrBasicAuthenticationError

""" 
http://localhost:8080/utd/API/utd/login
"""

class GnrCustomWebPage(object):
    py_requires='gnrcomponents/externalcall:BaseRpc'

    @public_method #http://localhost:8080/request/api/test
    def test(self,*args, **kwargs):
        self.request = self.request._request
        self.response = self.response._response
        print(x)


        
