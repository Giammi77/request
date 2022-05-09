# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('header', pkey='id', name_long='!![en]Header', name_plural='!![en]Headers',caption_field='key')
        self.sysFields(tbl, counter=True)
        tbl.column('request_id',size='22', group='_', name_long='Request'
                    ).relation('request.id', relation_name='header', mode='foreignkey', onDelete='raise')
        tbl.column('key', name_long='!![en]Key')
        tbl.column('value', name_long='!![en]Value')
        