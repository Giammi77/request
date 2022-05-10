# encoding: utf-8
import requests
from requests.auth import HTTPBasicAuth
import json
from gnr.core.gnrdecorator import public_method
class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('request', pkey='id', name_long='!![en]Request', name_plural='!![en]Requests',caption_field='endpoint')
        self.sysFields(tbl)

        tbl.column('endpoint', name_long='!![en]End Point')
        tbl.column('method_type', name_long='Method Type'
                    ).relation('method.type', relation_name='request', mode='foreignkey', onDelete='raise')
        tbl.column('body', name_long='!![en]Body')
        tbl.column('response', name_long='!![en]Response')
        tbl.column('debug', name_long='!![en]Debug')

    @public_method 
    def send(self, requestId=None, **kwargs):
        request = self.record(id=requestId, mode='bag')        
        url = request['endpoint']
        method = request['method_type']
        body = request['body']
        auth = None
        # params=dict(_callerpageid=self.db.currentPage.page_id, _debugmode=True)
        params=dict(_debugmode=True)

        headers=dict()

        headers_params = self.db.table('request.header').query(columns='$key,$value', where='$request_id=:requestId',requestId=request['id'], oreder_by='$_row_count').fetch()
        if len(headers_params)>0:
            for p in headers_params: 
                headers[p['key']]=p['value']

        qry_params = self.db.table('request.qry_param').query(columns='$key,$value', where='$request_id=:requestId',requestId=request['id'], oreder_by='$_row_count').fetch()
        if len(qry_params)>0:
            for p in qry_params: 
                params[p['key']]=p['value']
        params['request_id'] = requestId

        path_params = self.db.table('request.path_param').query(columns='$value', where='$request_id=:requestId',requestId=request['id'], oreder_by='$_row_count').fetch()
        if len(path_params)>0:
            for p in path_params: 
                url=url+'/'+p['value']

        r = requests.request(method,url,params=params,json=body,headers=headers,auth=auth,verify=False,allow_redirects=True)

        with self.recordToUpdate(request['id']) as rec:    
            rec['response'] = r.text
        self.db.commit()
        self.notifyDbUpdate(request['id'])

    def onDuplicating_many(self, record, copy_number=None, copy_label=None):
        record['endpoint'] = record['endpoint'] + '/Copia' + str(copy_number+1)
        
       
        