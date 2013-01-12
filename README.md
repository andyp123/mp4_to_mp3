MP4 TO MP3 CONVERSION SCRIPT
============================

mp4tomp3.py

A small Python script to convert mp4 video files to mp3 audio. Useful for turning video from sites such as www.ted.com into audio files useable
on any old mp3 player.
It uses mplayer and lame to do the actual conversion.

usage: python mp4tomp3.py [input directory [output directory]]
input directory (optional)  - set directory containing mp4 files to convert (defaults to current folder)
output directory (optional) - set directory to export mp3 files to (defaults to input)
example: python mp4tomp3.py ./video ./audio

NOTE: you will need python 2, mplayer and lame for this script to work
sudo apt-get install python2.7
sudo apt-get install mplayer
sudo apt-get install lame
