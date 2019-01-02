#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project: http://cloudedbats.org
# Copyright (c) 2018 Arnold Andreasson 
# License: MIT License (see LICENSE.txt or http://opensource.org/licenses/mit).

class MetadataBase():
    """ """
    def __init__(self):
        """ """
        self.clear()

    def clear(self):
        """ """
        self.metadata = {}
    
    def set_field(self, key, value):
        """ """
        if key and value:
            self.metadata[key] = value
    
    def get_field(self, key):
        """ """
        if key:
            return self.metadata.get(key, '')
    
    def get_metadata(self):
        """ """
        return self.metadata 
    
    def set_metadata(self, metadata):
        """ """
        for key, value in metadata.items():
            self.metadata[key] = value
