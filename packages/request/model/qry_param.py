# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('qry_param', pkey='id', name_long='!![en]Query Parameter', name_plural='!![en]Query Parameters',caption_field='key')
        self.sysFields(tbl,counter=True)
        tbl.column('request_id',size='22', group='_', name_long='Request'
                    ).relation('request.id', relation_name='qry_param', mode='foreignkey', onDelete='raise')
        tbl.column('key', name_long='!![en]Key')
        tbl.column('value', name_long='!![en]Value')
        