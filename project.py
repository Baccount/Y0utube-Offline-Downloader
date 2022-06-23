import os
import subprocess
import random
import string

# Youtube Offline Downloader


def main():
    # url = get_url()
    url = 'https://www.youtube.com/watch?v=Wch3gJG2GJ4'
    path = savePath()
    download_video(url, path)



def savePath():
    # return the path to save the video
    print('Choose directory to save video:')
    print('1. Current directory')
    print('2. Downloads')
    print('3. Documents')
    print('4. Desktop')
    choice = input('Enter your choice: ')
    if choice == '1':
        return os.getcwd()
    elif choice == '2':
        return os.path.join(os.path.expanduser('~'), 'Downloads')
    elif choice == '3':
        return os.path.join(os.path.expanduser('~'), 'Documents')
    elif choice == '4':
        return os.path.join(os.path.expanduser('~'), 'Desktop')
    else:
        print('Invalid choice')
        return savePath()
    
    return path




def get_url():
    url = input('Enter youtube url: ')
    return url


def red(text):
    # return text in red
    return '\033[31m' + text + '\033[0m'



# download youtube video and save it to a folder
def download_video(url, path):
    random_name = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(10))
    
    video_id = url.split('=')[1]
    video_path = path + '/' + random_name + '.mp4'
    if not os.path.exists(video_path):
        subprocess.call(['youtube-dl', '-f', 'mp4', '-o', video_path, url])






if __name__ == '__main__':
    main()