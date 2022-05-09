# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('path_param', pkey='id', name_long='!![en]Path Parameter', name_plural='!![en]Path Parameters',caption_field='value')
        self.sysFields(tbl,counter=True)
        tbl.column('request_id',size='22', group='_', name_long='Request'
                    ).relation('request.id', relation_name='path_param', mode='foreignkey', onDelete='raise')
        tbl.column('value', name_long='!![en]Value')
        