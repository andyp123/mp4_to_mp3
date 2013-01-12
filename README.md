<b>mp4tomp3.py</b>
<p>A small Python script to convert mp4 video files to mp3 audio. Useful for turning video from sites such as www.ted.com into audio files useable on any old mp3 player.<br>
It uses mplayer and lame to do the actual conversion.</p>

<b>usage</b>: python mp4tomp3.py [input directory [output directory]]<br>
&nbsp;&nbsp;<i><b>input directory</b></i> (optional) - set directory containing mp4 files to convert (defaults to current folder)<br>
&nbsp;&nbsp;<i><b>output directory</b></i> (optional) - set directory to export mp3 files to (defaults to input)<br>
<b>example</b>: python mp4tomp3.py ./video ./audio<br>

<b>Note</b>: you will need python 2, mplayer and lame for this script to work<br>
<pre>
sudo apt-get install python2.7
sudo apt-get install mplayer
sudo apt-get install lame
</pre>
