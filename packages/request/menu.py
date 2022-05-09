#!/usr/bin/python3
# -*- coding: utf-8 -*-

def config(root,application=None):
    root.thpage('!![en]Requests',table='request.request')
    service = root.branch('!![en]Service')
    service.thpage('!![en]Headers',table='request.header')
    service.thpage('!![en]Method Types',table='request.method')
    service.thpage('!![en]Path Parameters',table='request.path_param')
    service.thpage('!![en]Query Parameters',table='request.qry_param')

