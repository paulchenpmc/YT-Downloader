import os
import re
import argparse
import subprocess
from mutagen.easyid3 import EasyID3

download_command     = 'youtube-dl -x --audio-format mp3 --audio-quality 0 --embed-thumbnail {}'
brackets_remove_list = ['audio', 'video', 'lyric', 'lyrics']

# Download the youtube videos to mp3 file format using ffmpeg
def youtube_download(youtube_playlist_link):
    command = download_command.format(youtube_playlist_link)
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    while True:
        try:
            output = process.stdout.readline().decode()
            if output == '' and process.poll() is not None:
                break
            if output:
                print(output.strip())
        except:
            continue
    process.wait()
    if process.returncode != 0:
        print('Error occurred during download, exiting...')
        exit()

# Simple string processing on mp3 filenames to try and extract song metadata
def fill_metadata():
    mp3_filepath_list,mp3_file_list = [],[]
    # Find all mp3 files in subdirectories
    for root, dirs, files in os.walk(os.getcwd()):
        for file in files:
            if file.endswith(".mp3"):
                mp3_filepath_list.append(os.path.join(root, file))
                mp3_file_list.append(file)

    # Find and fill metadata for all mp3 files
    for filepath,filename in zip(mp3_filepath_list,mp3_file_list):
        # Clean filename
        remove_list = []
        match = re.search("(.*)(-.{11}.mp3)", filename) # Remove ffmpeg filenaming convention and .mp3 from filename
        remove_list.append(match[2])
        for keyword in brackets_remove_list:
            match = re.search(".*([\(\[].*{}.*[\)\]]).*".format(keyword), filename, re.IGNORECASE) # Remove anything in brackets like (official audio), etc
            if match is not None:
                remove_list.append(match[1])
        filename_cleaned = filename
        for word in remove_list:
            filename_cleaned = filename_cleaned.replace(word, '')
        # Extract artist and song title from filename
        dash_structure = re.search("(.*?) - (.*)", filename_cleaned)
        # Typical dash structure used in many youtube song videos (e.g. Artist - Song Title)
        if dash_structure is not None:
            artist = dash_structure[1]
            title  = dash_structure[2]
        # Assume Youtube video title is just the song name
        else:
            artist = None
            title  = filename_cleaned
        # Edit metadata
        audio = EasyID3(filepath)
        audio['title'] = title
        if artist:
            audio['artist'] = artist
        audio.save()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("playlist_link", help="The youtube playlist link to download and convert to audio.")
    args = parser.parse_args()
    youtube_playlist_link = args.playlist_link
    youtube_download(youtube_playlist_link)
    fill_metadata()