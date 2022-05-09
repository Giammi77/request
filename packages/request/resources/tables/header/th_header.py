#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('request_id')
        r.fieldcell('key')
        r.fieldcell('value')

    def th_order(self):
        return 'request_id'

    def th_query(self):
        return dict(column='key', op='contains', val='')

class ViewFromRequest(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('request_id')
        r.fieldcell('key',edit=True)
        r.fieldcell('value',edit=True)

    def th_order(self):
        return 'request_id'

    def th_query(self):
        return dict(column='key', op='contains', val='')

class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=2, border_spacing='4px')
        fb.field('request_id' )
        fb.field('key' )
        fb.field('value' )


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px' )
