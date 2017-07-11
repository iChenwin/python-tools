#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os

for filename in os.listdir('.'):
    if filename.endswith('.mkv'):
        with open('playlist.txt', 'a+') as bashFile:
            bashFile.write("file '" + filename + "'" + '\n')
            print filename