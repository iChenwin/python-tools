#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import subprocess

def getLength(filename):
    result = subprocess.Popen(["ffprobe", filename],
            stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
    return [x for x in result.stdout.readlines() if "Duration" in x]

for filename in os.listdir('.'):
    if filename.endswith('.mkv'):
        with open('draw.sh', 'a+') as bashFile:
            duration = getLength(filename)[0][12:20].replace(":", "：")
            cmd = "ffmpeg -t 00:00:30 -i " + filename + " -filter_complex \"drawtext=fontfile=/Library/Fonts/AdobeFangsongStd-Regular.otf: text='" + filename[-10:-4] + " %{pts\:gmtime\:0\:%H：%M：%S}/" + duration + "': x=5: y=5: fontsize=24: fontcolor=yellow@0.9: box=1: boxcolor=blue@0.6\" -c:a copy -c:v libx264 -preset veryfast -crf 16 -x264-params keyint=60 -map 0 " + filename[:-4] + "_d.mkv\n"
            bashFile.write(cmd)
            print cmd
