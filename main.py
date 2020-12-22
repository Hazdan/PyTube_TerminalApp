from pytube import YouTube
from winreg import *

with OpenKey(HKEY_CURRENT_USER, 'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders') as key:
    DOWNLOAD_PATH = QueryValueEx(key, '{374DE290-123F-4565-9164-39C4925E467B}')[0]



# GLOBAL VARIABLES

# These numbers represent the options in select_type_of_file()
MP4 = 1
MP3 = 2

# These numbers represent the options in select_download_mode()
SINGLE = 1
PLAYLIST = 2

# PATH OF THE DOWNLOAD FOLDER

def select_type_of_file():
    """
        Allows the user to select the type of file to download.

        Returns:
            int: returns the selected type
    """
    file_extension = None
    print('Enter the type of file you want to download')
    while file_extension != MP4 and file_extension != MP3:

        print("""
    1. MP4
    2. MP3
        """)
        file_extension = int(input())

        if file_extension != MP4 and file_extension != MP3:
            print('Enter a correct option')

    return file_extension


def select_download_mode():
    """
        Allows the user to select the download method, single or playlist

        Returns:
            int: returns the selected method
    """
    method = None
    print('Enter the download method')
    while method != SINGLE and method != PLAYLIST:
        print("""
    1. Single
    2. Playlist
        """)
        method = int(input())

        if method != SINGLE and method != PLAYLIST:
            print('Enter a correct option')

    return method


def run_download_process(file_extension, method):
    """
        Execute the download process depending on the options chosen by the user
        \n
        Parameters:\n
        file_extension (int): Representation of the type of file to download: MP3 or MP4\n
        method (int): Representation of the download method: SINGLE or PLAYLIST \n
        Returns:\n
            function: The download function\n
            or\n
            print: Print 'An error has occurred' if the download cannot be executed
    """

    if method == SINGLE:
        url = input('Enter youtube url:\n')

        if file_extension == MP4:
            return download_mp4_single(url)
        elif file_extension == MP3:
            return download_mp3_single(url)
        else:
            return print('An error has occurred')

    elif method == PLAYLIST:
        url = input('Enter url of youtube playlist:\n')

        if file_extension == MP4:
            return download_mp4_playlist(url)
        elif file_extension == MP3:
            return download_mp3_playlist(url)
        else:
            return print('An error has occurred')

    else:
        return print('An error has occurred')


def download_mp4_single(url):
    video = YouTube(url)
    stream = video.streams.get_by_itag('18')
    print('Downloading video...')
    stream.download(DOWNLOAD_PATH)
    print('The video has been downloaded successfully\n')
    return stream.default_filename




def download_mp3_single(url):
    print()
    return print('Sorry, this feature is not available yet')


def download_mp3_playlist(url):
    print()
    return print('Sorry, this feature is not available yet')


def main():
    print("""
         /$$$$$$$         /$$$$$$$$        /$$
        | $$__  $$       |__  $$__/       | $$
        | $$  \ $$ /$$   /$$| $$ /$$   /$$| $$$$$$$   /$$$$$$
        | $$$$$$$/| $$  | $$| $$| $$  | $$| $$__  $$ /$$__  $$
        | $$____/ | $$  | $$| $$| $$  | $$| $$  \ $$| $$$$$$$$
        | $$      | $$  | $$| $$| $$  | $$| $$  | $$| $$_____/
        | $$      |  $$$$$$$| $$|  $$$$$$/| $$$$$$$/|  $$$$$$$
        |__/       \____  $$|__/ \______/ |_______/  \_______/
                   /$$  | $$
                  |  $$$$$$/
                   \______/
         _               _                     _
        | |__   _  _    | |_    __ _   ___  __| |  __ _   _ _
        | '_ \ | || |   | ' \  / _` | |_ / / _` | / _` | | ' \ 
        |_.__/  \_, |   |_||_| \__,_| /__| \__,_| \__,_| |_||_|
                |__/

       ♠•♠ Downloading copyrighted YouTube videos is illegal ♠•♠
        ♦•♦ ♦•♦ I am not responsible for your downloads ♦•♦ ♦•♦
    """)
    while True:
        file_extension = select_type_of_file()
        method = select_download_mode()
        run_download_process(file_extension, method)



if __name__ == '__main__':
    main()