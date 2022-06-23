import os
import subprocess
import string
import youtube_dl

# Youtube Offline Downloader


def main():
    url = get_url()
    path = savePath()
    download_video(url, path)



def savePath():
    if read_save_path():
        # path is not None
        return read_save_path()
    
    # return the path to save the video
    print('Choose directory to save video:')
    print('1. Current directory')
    print('2. Downloads')
    print('3. Documents')
    print('4. Desktop')
    choice = input('Enter your choice: ')
    if choice == '1':
        path = os.getcwd()
    elif choice == '2':
        path = os.path.join(os.path.expanduser('~'), 'Downloads')
    elif choice == '3':
        path = os.path.join(os.path.expanduser('~'), 'Documents')
    elif choice == '4':
        path = os.path.join(os.path.expanduser('~'), 'Desktop')
    else:
        print('Invalid choice')
    
    save_path_to_file(path)
    return path













def save_path_to_file(path):
    with open('save_path.txt', 'w') as f:
        f.write(path)

def read_save_path():
    with open('save_path.txt', 'r') as f:
        return f.read()




def get_url():
    url = input('Enter youtube url: ')
    return url


def red(text):
    # return text in red
    return '\033[31m' + text + '\033[0m'



# download youtube video and save it to a folder
def download_video(url, save_path):
    ydl_opts = {
        # hight quality video
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/bestvideo+bestaudio',
        # save location of the video
        'outtmpl': save_path + '/%(title)s.%(ext)s',
    }
    id = url.strip()
    youtube_dl.YoutubeDL(ydl_opts).extract_info(id)




if __name__ == '__main__':
    main()