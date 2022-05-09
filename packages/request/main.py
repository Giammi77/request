#!/usr/bin/env python
# encoding: utf-8
from gnr.app.gnrdbo import GnrDboTable, GnrDboPackage

class Package(GnrDboPackage):
    def config_attributes(self):
        return dict(comment='request package',sqlschema='request',sqlprefix=True,
                    name_short='Request', name_long='Request', name_full='Request')
                    
    def config_db(self, pkg):
        pass
        
class Table(GnrDboTable):
    pass
