#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project: http://cloudedbats.org
# Copyright (c) 2018 Arnold Andreasson 
# License: MIT License (see LICENSE.txt or http://opensource.org/licenses/mit).

import re
import datetime
import dateutil.parser

import metadata4bats

class MetadataWavefileAudiomoth(metadata4bats.MetadataWavefile):
    """ """
    def __init__(self, dir_path, file_name=None):
        """ """
        super().__init__(dir_path, file_name)
        self.clear()
    
    def clear(self):
        """ """
        super().clear()
    
    def extract_metadata(self):
        """ """
        super().extract_metadata()
        
        # Check if the filename contains datetime as HEX in Unix epoch. 
        # Filename example: '59CD4D0D.WAV'
        file_stem = self.file_path.stem
        hexaPattern = re.compile(r"^([0-9a-fA-F]+)$")
        m = re.search(hexaPattern, file_stem)
        if m is not None:
            posix_time = int(file_stem, 16)
            self.rec_datetime_utc = datetime.datetime.utcfromtimestamp(posix_time)
            self.set_field('rec_datetime_utc', self.rec_datetime_utc.strftime('%Y-%m-%dT%H:%M:%SZ'))
            
#             print("Regexp match: ", m.group(1))
#             print('String in ISO format: ', self.rec_datetime_utc.strftime('%Y-%m-%dT%H:%M:%SZ'))
#             print('String in compact ISO format: ', self.rec_datetime_utc.strftime('%Y%m%dT%H%M%SZ'))

        # Get more meatdata from file header.
        # Example: "Recorded at 19:27:09 28/09/2017 (UTC) by AudioMoth 0FE081F80FE081F0 at gain setting 2 while battery state was > 5.0 V"
        hexaPattern = re.compile(b"Recorded at (.*) by AudioMoth (.*) at gain setting (.*) while battery state")
        with open(self.file_path, 'rb') as f:
            buffer = f.read(256)
            
        m = re.search(hexaPattern, buffer)
        if m is not None:
            date_time = dateutil.parser.parse(m.group(1).decode('utf-8').replace('(UTC)', ''))
            self.rec_datetime_utc = date_time.strftime('%Y-%m-%dT%H:%M:%SZ')
            self.detector_model = 'AudioMoth'
            self.detector_manufacturer = 'https://www.openacousticdevices.info'
            self.detector_id = m.group(2).decode('utf-8')
            self.detector_gain_setting = m.group(3).decode('utf-8')

            self.set_field('rec_datetime_utc', self.rec_datetime_utc)
            self.set_field('rec_audiomoth_id', self.detector_id)
            self.set_field('rec_audiomoth_gain', self.detector_gain_setting)
            
#             print('TEST: ', date_time.strftime('%Y-%m-%dT%H:%M:%SZ'))
#             print("Regexp match: ", m.group(0).decode('utf-8'))
#             print("Regexp match: ", m.group(1).decode('utf-8'))
#             print("Regexp match: ", m.group(2).decode('utf-8'))
#             print("Regexp match: ", m.group(3).decode('utf-8'))



if __name__ == '__main__':
    """ """
    import pprint
    
    print('CloudedBats - metadata - test')

    mw = MetadataWavefileAudiomoth('/home/arnold/Desktop/batfiles', 
                                   '59CD4D0D.WAV')
    mw.extract_metadata()
#     print('Length: ', len(mw.get_wave_data()))
    print('Metadata: ')
    pp = pprint.PrettyPrinter(indent=1)
    pp.pprint(mw.metadata)
