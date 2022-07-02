import os
import re  # regex
from time import sleep

import youtube_dl
from pyfiglet import Figlet


def choice1(url: str = None):
    # download video
    if url is None:
        url = input('Enter the url: ')
    while check_url(url) is None:
        url = input('Enter the url : ')
    savedPath = read_save_path()
    save_path = savedPath if savedPath != '' else savePath()
    download_video(url=url, save_path=save_path)

def choice3(url: str = None):
    # download playlist
    if url is None:
        url = input('Enter the url: ')
    while check_url(url) is None:
        url = input('Enter the url : ')
    savedPath = read_save_path()
    save_path = savedPath if savedPath != '' else savePath()
    download_playlist(url=url, save_path=save_path)

def savePath(path: str = None):
    # User provided path to save the video
    if path is not None:
        save_path_to_file(path)
        clear_screen()
        print(green('Saved new default path'))
        sleep(1)
        return
    defaultPath = read_save_path()
    clear_screen()
    # return the path to save the video
    print('Choose directory to save video:')
    print('1. Current directory')
    print('2. Downloads')
    print('3. Documents')
    print('4. Desktop')
    print('5. Custom path')
    print('6. Exit')
    print('')
    if defaultPath:
        print(green(f'Current Default path = {defaultPath}'))
    choice = input('Enter your choice: ')
    path = ''
    if choice == '1':
        path = os.getcwd()
    elif choice == '2':
        path = os.path.join(os.path.expanduser('~'), 'Downloads')
    elif choice == '3':
        path = os.path.join(os.path.expanduser('~'), 'Documents')
    elif choice == '4':
        path = os.path.join(os.path.expanduser('~'), 'Desktop')
    elif choice == '5':
        # return the user chosen path to save the video
        clear_screen()
        path = userPath()
    elif choice == '6':
        return
    else:
        # re-ask the user to choose a directory
        savePath()

    save_path_to_file(path)
    return path


def userPath():
    # Get user folder path and validate it
    path = input('Enter the path: ')
    if os.path.exists(path):
        return path
    else:
        clear_screen()
        print(red('Path does not exist'))
        userPath()


def show_splash():
    '''
    Display splash screen
    '''
    clear_screen()
    title = 'Y0utube Offline Downloader'
    f = Figlet(font='standard')
    print(red(f.renderText(title)))


def clear_screen():
    print('\n' * 25)


def save_path_to_file(path):
    with open('save_path.txt', 'w') as f:
        f.write(path)


def read_save_path():
    if os.path.exists('save_path.txt'):
        with open('save_path.txt', 'r') as f:
            return f.read()
    return ''


def check_url(url: str):
    # check if the url is valid
    regex = (
        r"^(https?\:\/\/)?(www\.youtube\.com|youtu\.be)\/.+$")

    match = re.match(regex, url)
    if match:
        return match.group()
    elif match is None:
        return None


def green(text: str):
    # return text in green
    return '\033[32m' + text + '\033[0m'


def red(text: str):
    # return text in red
    return '\033[31m' + text + '\033[0m'


def blue(text: str):
    # return text in blue
    return '\033[34m' + text + '\033[0m'


def download_video(url: str, save_path: str):
    # download youtube video and save it to a folder
    ydl_opts = {
        # hight quality video
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/bestvideo+bestaudio',
        # save location of the video
        'outtmpl': save_path + '/%(title)s.%(ext)s',
    }
    youtube_dl.YoutubeDL(ydl_opts).extract_info(url)


def download_playlist(url: str, save_path: str):
    # download playlist from youtube using youtube-dl

    ydl_opts = {
        # hight quality video
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/bestvideo+bestaudio',
        # save location of the video
        'outtmpl': save_path + '/%(title)s.%(ext)s',
        'yes-playlist': True,
    }
    youtube_dl.YoutubeDL(ydl_opts).extract_info(url)
