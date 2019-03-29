#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project: http://cloudedbats.org
# Copyright (c) 2018 Arnold Andreasson 
# License: MIT License (see LICENSE.txt or http://opensource.org/licenses/mit).

import pathlib
import wave

import metadata4bats

class MetadataWavefile(metadata4bats.MetadataBase):
    """ """
    def __init__(self, dir_path, file_name=None):
        """ """
        super().__init__()
        self.clear()
        
        self.file_path = None
        if file_name is None:
            self.file_path = pathlib.Path(dir_path)
        else:
            self.file_path = pathlib.Path(dir_path, file_name)

    def clear(self):
        """ """
        super().clear()
    
    def extract_metadata(self):
        """ """
        try:
            # File and directory info.
            self.set_field('rec_file_path', str(self.file_path))
            self.set_field('rec_abs_file_path', str(self.file_path.absolute().resolve()))
            self.set_field('rec_dir_path', str(self.file_path.parent))
            self.set_field('rec_file_name', self.file_path.name)
            self.set_field('rec_file_stem', self.file_path.stem)
        except:
            pass
        
        try:
            # Standard wave file metadata.
            with wave.open(str(self.file_path), 'r') as wave_file:
                self.nchannels = wave_file.getnchannels() # 1=mono, 2=stereo.
                self.sampwidth = wave_file.getsampwidth() # sample width in bytes.
                self.framerate = wave_file.getframerate() # Sampling frequency.
                self.nframes = wave_file.getnframes() # Number of audio frames.
            #
            self.set_field('rec_nchannels', self.nchannels)
            self.set_field('rec_sampwidth', self.sampwidth)
            self.set_field('rec_framerate', self.framerate)
            self.set_field('rec_nframes', self.nframes)
            #
            if int(self.framerate > 90000):
                frame_rate_hz = self.framerate
                lenght_s = int(self.nframes) / int(self.framerate)
            else:
                # Probably time division by a factor of 10.
                frame_rate_hz = self.framerate * 10
                lenght_s = int(self.nframes) / int(self.framerate) / 10
            self.set_field('rec_frame_rate_hz', self.framerate)
            self.set_field('rec_lenght_s', int(lenght_s))
            #
        except:
            pass
