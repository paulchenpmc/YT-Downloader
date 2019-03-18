# YT-Downloader

### Wow, what the heck does this tool even do?
Great question. This tool is a user-friendly wrapper for the [youtube-dl command line program](https://github.com/ytdl-org/youtube-dl) with a couple extra bells and whistles. The intent of this tool is to provide a one-click solution to batch download playlists, and try to intelligently fill song metadata.

### Installation:
1. Ensure prerequisites are installed
    1. [ffmpeg tool](https://ffmpeg.zeranoe.com/builds/)
        1. Add /path/to/ffmpeg_folder/bin to your PATH environment variable
    2. [Youtube-dl tool](https://yt-dl.org/latest/youtube-dl.exe)
        1. Move youtube-dl.exe to /path/to/ffmpeg_folder/bin
    3. Python 3
        1. Install [python 3](https://www.python.org/downloads/), make sure to tick the box adding it to your PATH variable!
        2. Install the python module mutagen. Open command prompt and enter the following:
        `pip install mutagen`
2. Clone/download the YT-Downloader repository to your computer

### Usage:
1. Double click the download.bat file
2. Copy + paste a youtube playlist link into the command prompt window
3. Press enter
4. Wait for the download to finish