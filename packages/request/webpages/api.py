#!/usr/bin/python3
# -*- coding: utf-8 -*-
from gnr.core.gnrdecorator import public_method
import json
from datetime import datetime
import hashlib

# from gnr.web.gnrwebpage import GnrBasicAuthenticationError

""" 
http://localhost:8080/request/api/test
"""

class GnrCustomWebPage(object):
    py_requires='gnrcomponents/externalcall:BaseRpc'

    def debug(self,dati):
        with self.db.table('request.request').recordToUpdate(self.requestId ) as rec:    
            rec['debug'] = dati
        self.db.commit()
        self.db.table('request.request').notifyDbUpdate(self.requestId)
        return 

    @public_method #http://localhost:8080/request/api/test
    def test(self,*args, **kwargs):
        self.request = self.request._request
        self.response = self.response._response
        self.requestId = kwargs['request_id']
        # print('here!!')
        # print(self.requestId)
        # print(dir(self.request))
        # self.debug(self.request.data)
        return 
        # if self.request.method == 'POST':
        #     json = self.request.json
        #     self.debug('pippo prova')