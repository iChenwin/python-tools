#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os

for filename in os.listdir('.'):
    if filename.endswith('.mkv'):
        newName = "MontyPythonsFlyingCircus" + filename[-16:-10] + ".mkv"
        os.rename(os.path.join('.', filename), os.path.join('.', newName))
        print filename + ' --> ' + newName