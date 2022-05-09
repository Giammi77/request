# encoding: utf-8
from gnr.core.gnrdecorator import metadata
class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('method', pkey='type', name_long='!![en]Method Type', name_plural='!![en]Method Types',caption_field='type')
        self.sysFields(tbl, id=False )
        tbl.column('type', name_long='Type')
    
    @metadata(mandatory=True)
    def sysRecord_GET(self):
        return self.newrecord(type = 'GET')
    @metadata(mandatory=True)
    def sysRecord_PUT(self):
        return self.newrecord(type = 'PUT')
    @metadata(mandatory=True)
    def sysRecord_POST(self):
        return self.newrecord(type = 'POST')
    @metadata(mandatory=True)
    def sysRecord_DELETE(self):
        return self.newrecord(type = 'DELETE')