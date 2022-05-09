# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('test', pkey='id', name_long='!![en]Test', name_plural='!![en]Tests',caption_field='test')
        self.sysFields(tbl)
        tbl.column('test', name_long='Test')
        