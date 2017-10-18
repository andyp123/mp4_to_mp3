# MP4 TO MP3 CONVERSION SCRIPT
# script to convert mp4 video files to mp3 audio
# useful for turning video ripped from sites such as Youtube or TED
# into audio files useable with any old mp3 player.
#
# usage: python mp4tomp3.py [input directory [output directory]]
# input directory (optional)  - set directory containing mp4 files to convert (defaults to current folder)
# output directory (optional) - set directory to export mp3 files to (defaults to input)
#
# NOTE: you will need python (2 or 3), mplayer and lame for this script to work
# sudo apt-get install lame
# sudo apt-get install mplayer
# sudo apt-get install python2.7   -- for python 2
# sudo apt-get install python3.6   -- for python 3

from __future__ import print_function   # for compatibility with both python 2 and 3
from subprocess import call             # for calling mplayer and lame
from sys import argv                    # allows user to specify input and output directories
import os                               # help with file handling

def check_file_exists(directory, filename, extension):
    path = directory + "/" + filename + extension
    return os.path.isfile(path)

def main(indir, outdir):


    try:
        # check specified folders exist
        if not os.path.exists(indir):
            exit("Error: Input directory \'" + indir + "\' does not exist. (try prepending './')")
        if not os.path.exists(outdir):
            exit("Error: Output directory \'" + outdir + "\' does not exist.")
        if not os.access(outdir, os.W_OK):
            exit("Error: Output directory \'" + outdir + "\' is not writeable.")

        print("[{0}/*.mp4] --> [{1}/*.mp3]".format(indir, outdir))
        files = [] # files for exporting
            
        # get a list of all convertible files in the input directory
        filelist = [ f for f in os.listdir(indir) if f.endswith(".mp4") ]
        for path in filelist:
            basename = os.path.basename(path) 
            filename = os.path.splitext(basename)[0]
            files.append(filename)
        # remove files that have already been outputted from the list
        files[:] = [f for f in files if not check_file_exists(outdir, f, ".mp3")]
    except OSError as e:
        exit(e)
    
    if len(files) == 0:
        exit("Could not find any files to convert that have not already been converted.")

    # convert all unconverted files
    for filename in files:
        print("-- converting {0}/{2}.mp4 to {1}/{2}.mp3 --".format(indir, outdir, filename))
        call(["mplayer", "-novideo", "-nocorrect-pts", "-ao", "pcm:waveheader", indir + "/" + filename + ".mp4"])
        call(["lame", "-v", "audiodump.wav", outdir + "/" + filename + ".mp3"])
        os.remove("audiodump.wav")

# set the default directories and try to get input directories
args = [".", "."]
for i in range(1, min(len(argv), 3)):
    args[i - 1] = argv[i]

# if only input directory is set, make the output directory the same
if len(argv) == 2:
    args[1] = args[0]

main(args[0], args[1])
