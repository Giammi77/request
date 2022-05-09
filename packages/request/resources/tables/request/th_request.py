#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('endpoint')
        r.fieldcell('method_type')
        r.fieldcell('body')

    def th_order(self):
        return 'endpoint'

    def th_query(self):
        return dict(column='endpoint', op='contains', val='')



class Form(BaseComponent):

    def th_form(self, form):
        bc=form.center.borderContainer(datapath='.record')
        fb = bc.contentPane(region='top',splitter=True).formbuilder(cols=2, border_spacing='4px')
        fb.field('endpoint', width='50em', colspan=2)
        fb.field('method_type', width='10em', hasDownArrow=True)
        fb.button('Send').dataRpc(self.db.table('request.request').send,
                               requestId='=.id',
                               _lockScreen=True)
        fb.onDbChanges("this.form.reload();" , table='request.request')

        tc = bc.tabContainer(region='center')

        tc.contentPane(title='!![en]Query Parameters').inlineTableHandler(relation='@qry_param', datapath='#FORM.qry_parma', viewResource='ViewFromRequest')
        tc.contentPane(title='!![en]Path Parameters').inlineTableHandler(relation='@path_param', datapath='#FORM.path_parma', viewResource='ViewFromRequest')
        tc.contentPane(title='!![en]Headers').inlineTableHandler(relation='@header', datapath='#FORM.header', viewResource='ViewFromRequest')
        tc.contentPane(title='!![en]Authorization')
        tc.contentPane(title='!![en]Body',margin='25px').simpleTextArea(value='^.body', height='500px')
        tc.contentPane(title='!![en]Response').simpleTextArea(value='^.response', height='600px')
        tc.contentPane(title='!![en]Debug').simpleTextArea(value='^.debug', height='600px')

    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px' )
