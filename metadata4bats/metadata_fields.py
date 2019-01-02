#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project: http://cloudedbats.org
# Copyright (c) 2018 Arnold Andreasson 
# License: MIT License (see LICENSE.txt or http://opensource.org/licenses/mit).

class MetadataFields():
    """ Contains a dictionary with all used metadata fields. """
    
    def __init__(self):
        """ """
        self.fields = None
        self.internal_key_lookup = {}
        self.synonym_lookup = {}
        self.guano_lookup = {}
        self.darwincore_lookup = {}
    
    def get_by_internal_key(self, internal_key, key=None):
        """ """
        self._load_fields()
        metadata_dict = self.internal_key_lookup.get(internal_key, {})
        if key is None:
            return metadata_dict
        elif key in ['internal_key', 'type', 'default']:
            return metadata_dict.get(key, '')
        elif key in ['gui', 'guano', 'dwc']:
            return metadata_dict['export'].get(key, '')
    
    def get_by_synonym(self, synonym, key=None):
        """ """
        self._load_fields()
        metadata_dict = self.synonym_lookup.get(synonym, {})
        if key is None:
            return metadata_dict
        elif key in ['internal_key', 'type', 'default']:
            return metadata_dict.get(key, '')
        elif key in ['gui', 'guano', 'dwc']:
            return metadata_dict['export'].get(key, '')
    
    def get_by_guano_key(self, guano_key, key=None):
        """ """
        self._load_fields()
        metadata_dict = self.guano_lookup.get(guano_key, {})
        if key is None:
            return metadata_dict
        elif key in ['internal_key', 'type', 'default']:
            return metadata_dict.get(key, '')
        elif key in ['gui', 'guano', 'dwc']:
            return metadata_dict['export'].get(key, '')
    
    def get_by_dwc_key(self, darwincore_key, key=None):
        """ """
        self._load_fields()
        metadata_dict = self.darwincore_lookup.get(darwincore_key, {})
        if key is None:
            return metadata_dict
        elif key in ['internal_key', 'type', 'default']:
            return metadata_dict.get(key, '')
        elif key in ['gui', 'guano', 'dwc']:
            return metadata_dict['export'].get(key, '')
    
    
    def _load_fields(self):
        """ """
        # If not loaded before.
        if self.fields is None:
            # Load all field definitions.
            self._define_fields()
            # Create lookup dictionaries.
            for field_dict in self.fields:
                self.internal_key_lookup[field_dict['internal_key']] = field_dict
                self.guano_lookup[field_dict['export']['guano']] = field_dict
                self.darwincore_lookup[field_dict['export']['dwc']] = field_dict
                # Synonyms lookup also contains internal_key and export names. 
                self.synonym_lookup[field_dict['internal_key']] = field_dict
                for synonym in field_dict['synonyms']:
                    self.synonym_lookup[synonym] = field_dict
                for export_value in field_dict['export'].values():
                    self.synonym_lookup[export_value] = field_dict
        # Cleanup empty keys:
        if '' in self.internal_key_lookup: del self.internal_key_lookup['']
        if '' in self.synonym_lookup: del self.synonym_lookup['']
        if '' in self.guano_lookup: del self.guano_lookup['']
        if '' in self.darwincore_lookup: del self.darwincore_lookup['']
        
    
    def _define_fields(self):
        """ """
        self.fields = [
            # Wave file and directory info.
            {   'internal_key': 'rec_file_path', 
                'type': 'string', 
                'default': '', 
                'synonyms': ['', '', ],  
                'export': { 'gui': '', 'guano': '', 'dwc': '', }, 
            },
            {   'internal_key': 'rec_abs_file_path', 
                'type': 'string', 
                'default': '', 
                'synonyms': ['', '', ],  
                'export': { 'gui': '', 'guano': '', 'dwc': '', }, 
            },
            {   'internal_key': 'rec_dir_path', 
                'type': 'string', 
                'default': '', 
                'synonyms': ['', '', ],  
                'export': { 'gui': '', 'guano': '', 'dwc': '', }, 
            },
            {   'internal_key': 'rec_file_name', 
                'type': 'string', 
                'default': '', 
                'synonyms': ['', '', ],  
                'export': { 'gui': '', 'guano': '', 'dwc': '', }, 
            },
            {   'internal_key': 'rec_file_stem', 
                'type': 'string', 
                'default': '', 
                'synonyms': ['', '', ],  
                'export': { 'gui': '', 'guano': '', 'dwc': '', }, 
            },

            # Wave file standard metadata.
            {   'internal_key': 'rec_nchannels', 
                'type': 'int', 
                'default': '', 
                'synonyms': ['', '', ],  
                'export': { 'gui': '', 'guano': '', 'dwc': '', }, 
            },
            {   'internal_key': 'rec_sampwidth', 
                'type': 'int', 
                'default': '', 
                'synonyms': ['', '', ],  
                'export': { 'gui': '', 'guano': '', 'dwc': '', }, 
            },
            {   'internal_key': 'rec_framerate', 
                'type': 'int', 
                'default': '', 
                'synonyms': ['', '', ],  
                'export': { 'gui': '', 'guano': '', 'dwc': '', }, 
            },
            {   'internal_key': 'rec_nframes', 
                'type': 'int', 
                'default': '', 
                'synonyms': ['', '', ],  
                'export': { 'gui': '', 'guano': '', 'dwc': '', }, 
            },

            # WURB metadata.
            {   'internal_key': 'rec_framerate_hz', 
                'type': 'int', 
                'default': '', 
                'synonyms': ['', '', ],  
                'export': { 'gui': '', 'guano': '', 'dwc': '', }, 
            },
            {   'internal_key': 'rec_file_framerate_hz', 
                'type': 'int', 
                'default': '', 
                'synonyms': ['', '', ],  
                'export': { 'gui': '', 'guano': '', 'dwc': '', }, 
            },

            # AudioMoth metadata.
            {   'internal_key': 'rec_audiomoth_id', 
                'type': 'string', 
                'default': '', 
                'synonyms': ['', '', ],  
                'export': { 'gui': '', 'guano': '', 'dwc': '', }, 
            },
            {   'internal_key': 'rec_audiomoth_gain', 
                'type': 'int', 
                'default': '', 
                'synonyms': ['', '', ],  
                'export': { 'gui': '', 'guano': '', 'dwc': '', }, 
            },
            {   'internal_key': 'rec_comment', 
                'type': 'string', 
                'default': '', 
                'synonyms': ['', '', ],  
                'export': { 'gui': '', 'guano': '', 'dwc': '', }, 
            },

            # Detector location and time.
            {   'internal_key': 'rec_latitude_dd', 
                'type': 'float', 
                'default': '0.00', 
                'synonyms': ['lat', 'latitude', ],  
                'export': { 'gui': 'Latitude (DD)', 'guano': 'Loc latitude', 'dwc': 'latitudeDD', }, 
            },
            {   'internal_key': 'rec_longitude_dd', 
                'type': 'float', 
                'default': '', 
                'synonyms': ['lon', 'long', 'longitude', ],  
                'export': { 'gui': '', 'guano': 'Loc longitude', 'dwc': 'longitudeDD', }, 
            },
            {   'internal_key': 'rec_datetime_local', 
                'type': 'string', 
                'default': '', 
                'synonyms': ['', '', ],  
                'export': { 'gui': '', 'guano': '', 'dwc': '', }, 
            },
            {   'internal_key': 'rec_datetime_utc', 
                'type': 'string', 
                'default': '', 
                'synonyms': ['', '', ],  
                'export': { 'gui': '', 'guano': '', 'dwc': '', }, 
            },
            {   'internal_key': '', 
                'type': '', 
                'default': '', 
                'synonyms': ['', '', ],  
                'export': { 'gui': '', 'guano': '', 'dwc': '', }, 
            },
            
            # From GUANO:

            # _coersion_rules = {
            #     'Filter HP': float, 
            #     'Length': float, 
            #     'Loc Elevation': float,
            #     'Loc Accuracy': int, 
            #     'Samplerate': int,
            #     'TE': lambda value: int(value) if value else 1,
            #     'Loc Position': lambda value: tuple(float(v) for v in value.split()),
            #     'Timestamp': parse_timestamp,
            #     'Note': lambda value: value.replace('\\n', '\n'),
            # }
            # _serialization_rules = {
            #     'Loc Position': lambda value: '%f %f' % value,
            #     'Timestamp': lambda value: value.isoformat() if value else '',
            #     'Length': lambda value: '%.2f' % value,
            #     'Note': lambda value: value.replace('\n', '\\n')
            # }
        
            {   'internal_key': 'latlong_dd', 
                'type': 'float-float', 
                'default': '', 
                'synonyms': ['', '', ],  
                'export': { 'gui': '', 'guano': 'Loc Position', 'dwc': '', }, 
            },
            {   'internal_key': 'datetime', 
                'type': 'datetime', 
                'default': '', 
                'synonyms': ['', '', ],  
                'export': { 'gui': '', 'guano': 'Timestamp', 'dwc': '', }, 
            },
            {   'internal_key': 'record_length_s', 
                'type': 'int', 
                'default': '', 
                'synonyms': ['', '', ],  
                'export': { 'gui': '', 'guano': 'Length', 'dwc': '', }, 
            },
            {   'internal_key': 'record_note', 
                'type': 'text', 
                'default': '', 
                'synonyms': ['', '', ],  
                'export': { 'gui': '', 'guano': 'Note', 'dwc': '', }, 
            },
            {   'internal_key': 'te_factor', 
                'type': 'int', 
                'default': '', 
                'synonyms': ['', '', ],  
                'export': { 'gui': '', 'guano': 'TE', 'dwc': '', }, 
            },
            {   'internal_key': 'samplerate_hz', 
                'type': 'int', 
                'default': '', 
                'synonyms': ['', '', ],  
                'export': { 'gui': '', 'guano': 'Samplerate', 'dwc': '', }, 
            },
            {   'internal_key': 'location_accuracy', 
                'type': 'int', 
                'default': '', 
                'synonyms': ['', '', ],  
                'export': { 'gui': '', 'guano': 'Loc Accuracy', 'dwc': '', }, 
            },
            {   'internal_key': '', 
                'type': 'float', 
                'default': '', 
                'synonyms': ['', '', ],  
                'export': { 'gui': '', 'guano': 'Loc Elevation', 'dwc': '', }, 
            },
            {   'internal_key': '', 
                'type': 'float', 
                'default': '', 
                'synonyms': ['', '', ],  
                'export': { 'gui': '', 'guano': 'Length', 'dwc': '', }, 
            },
            {   'internal_key': '', 
                'type': 'float', 
                'default': '', 
                'synonyms': ['', '', ],  
                'export': { 'gui': '', 'guano': 'Filter HP', 'dwc': '', }, 
            },
                        
#             {   'internal_key': '', 
#                 'type': '', 
#                 'default': '', 
#                 'synonyms': ['', '', ],  
#                 'export': { 'gui': '', 'guano': '', 'dwc': '', }, 
#             },
#             {   'internal_key': '', 
#                 'type': '', 
#                 'default': '', 
#                 'synonyms': ['', '', ],  
#                 'export': { 'gui': '', 'guano': '', 'dwc': '', }, 
#             },
        ]


### TEST ###

if __name__ == '__main__':
    """ """
    print('CloudedBats - metadata - test')
    
    metadata = MetadataFields()
    
    print('Dict: ', metadata.get_by_internal_key('rec_latitude_dd'))
    print('Key: ', metadata.get_by_internal_key('rec_latitude_dd', 'type'))
    print('Dict: ', metadata.get_by_synonym('lat'))
    print('Key: ', metadata.get_by_synonym('latitude', 'default'))
    print('Dict: ', metadata.get_by_guano_key('Loc latitude'))
    print('Key: ', metadata.get_by_guano_key('Loc latitude', 'type'))
    print('Dict: ', metadata.get_by_dwc_key('latitudeDD'))
    print('Key: ', metadata.get_by_dwc_key('latitudeDD', 'type'))

