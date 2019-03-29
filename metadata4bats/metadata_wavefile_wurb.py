#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project: http://cloudedbats.org
# Copyright (c) 2018 Arnold Andreasson 
# License: MIT License (see LICENSE.txt or http://opensource.org/licenses/mit).

import re

import metadata4bats

class MetadataWavefileWurb(metadata4bats.MetadataWavefile):
    """ """
    def __init__(self, dir_path, file_name=None):
        """ """
        super().__init__(dir_path, file_name)
        self.clear()
    
    def clear(self):
        """ """
        super().clear()
    
    def extract_metadata(self):
        """ Used to extract file name parts from sound files created by CloudedBats-WURB.
            Format: <recorder-id>_<time>_<position>_<rec-type>_<comments>.wav
            Example: wurb1_20170611T005215+0200_N57.6548E12.6711_TE384_Mdau-in-tandem.wav
        """
        super().extract_metadata()
        
        # Extract parts based on format.
        parts = self.file_path.stem.split('_')
        
        # Check if the file is a WURB generated/formatted file.
        self.set_field('wurb_format', False)
        if self.file_path.suffix.lower() not in ['.wav']:
            return
        if len(parts) >= 4:
            rec_type = parts[3]
            if (len(rec_type) >= 4) and \
               (parts[3][0:2] in ['TE', 'FS']):
                pass
            else:
                return
        else:
            return
        #
#         self.set_field('wurb_format', True)
                
        # Detector id.
        if len(parts) > 0:
            self.set_field('rec_detector_id', parts[0])
            
        # Datetime in ISO format.
        if len(parts) > 1:
            try:
                self.set_field('rec_datetime_local', parts[1])
            except:
                pass
        
        # Latitude/longitude.
        if len(parts) > 2:
            latlong_str = parts[2].upper()
            self.set_field('rec_latlong_str', latlong_str)
            # Extract lat-DD and long-DD.
            try:
                ns_start = re.search(r'[NS]', latlong_str).span(0)[0]
                ew_start = re.search(r'[EW]', latlong_str).span(0)[0]
                latitude_dd = float(latlong_str[ns_start+1:ew_start])
                longitude_dd = float(latlong_str[ew_start+1:])
                if latlong_str[ns_start] == 'S':
                    latitude_dd *= -1.0
                if latlong_str[ew_start] == 'W':
                    longitude_dd *= -1.0
                self.set_field('rec_latitude_dd', latitude_dd)
                self.set_field('rec_longitude_dd', longitude_dd)
            except:
                pass
        
        # Framerates.
        if len(parts) > 3:
            self.set_field('rec_type', parts[3])
            try:
                frame_rate = float(parts[3][2:])
                self.set_field('rec_frame_rate_hz', str(round(frame_rate * 1000.0)))
                if parts[3][0:2] == 'TE':
                    self.set_field('rec_is_te', True) # TE, Time Expanded.
                    self.set_field('rec_file_framerate_hz', str(round(frame_rate * 100.0)))
                else:
                    self.set_field('rec_is_te', False) # FS, Full Scan.
                    self.set_field('rec_file_framerate_hz', str(round(frame_rate * 1000.0)))
            except:
                pass
        
        # Comments. All parts above index 4.
        if len(parts) > 4:
            self.set_field('rec_comment', '_'.join(parts[4:]))



if __name__ == '__main__':
    """ """
    import pprint
    
    print('CloudedBats - metadata - test')

    mw = MetadataWavefileWurb('/home/arnold/Desktop/batfiles', 
                                   'WURB2_20180908T212225+0200_N57.6627E12.6393_TE384_Myotis.wav')
    mw.extract_metadata()
#     print('Length: ', len(mw.get_wave_data()))
    print('Metadata: ')
    pp = pprint.PrettyPrinter(indent=1)
    pp.pprint(mw.metadata)
