import os
import subprocess
import string
import youtube_dl
from pyfiglet import Figlet
from time import sleep
import re

# Youtube Offline Downloader


def main():
    clear_screen()
    show_splash()
    print('1. Download video')
    print('2. Default Download Location')
    print('3. Exit')
    choice = input('Enter your choice: ')
    if choice == '1':
        url = input('Enter the url : ')
        while check_url(url) is None:
            url = input('Enter the url : ')
        savedPath = read_save_path()
        save_path = savedPath if savedPath != '' else savePath()
        download_video(url, save_path)
    elif choice == '2':
        savePath()
        main()
    elif choice == '3':
        print('Exiting...')
        exit()



def savePath():
    defaultPath = read_save_path()
    clear_screen()
    # return the path to save the video
    print('Choose directory to save video:')
    print('1. Current directory')
    print('2. Downloads')
    print('3. Documents')
    print('4. Desktop')
    print('5. Custom')
    if  defaultPath:
        print(red(f'Current Default path = {defaultPath}'))
        
        
        
        
        
        
        
        
        
        
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
    else:
        # reask the user to choose a directory
        savePath()
    
    save_path_to_file(path)
    return path


def show_splash():
    '''
    Display splash screen
    '''
    clear_screen()
    title = 'Youtube Offline Downloader'
    figlet = Figlet()
    fonts = figlet.getFonts()
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
        regex = (
            r"^(https?\:\/\/)?(www\.youtube\.com|youtu\.be)\/.+$")

        match = re.match(regex, url)
        if match:
            return match.group()
        elif match is None:
            return None



def red(text: str):
    # return text in red
    return '\033[31m' + text + '\033[0m'

def blue(text: str):
    # return text in blue
    return '\033[34m' + text + '\033[0m'


# download youtube video and save it to a folder
def download_video(url: str, save_path: str):
    
    ydl_opts = {
        # hight quality video
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/bestvideo+bestaudio',
        # save location of the video
        'outtmpl': save_path + '/%(title)s.%(ext)s',
    }
    youtube_dl.YoutubeDL(ydl_opts).extract_info(url)




if __name__ == '__main__':
    main()