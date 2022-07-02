from project_func import check_url, green, red, blue, clear_screen, show_splash, savePath, read_save_path, download_video, download_playlist, choice1
import sys
import argparse as ap



# Youtube Offline Downloader

def main():
    # get arguments from user using argparse module for only the url
    parser = ap.ArgumentParser(description='Youtube Offline Downloader')
    parser.add_argument('-u', '--url', help='URL of the video or playlist to download', required=False)
    parser.add_argument('-p', '--path', help='Path to save the video or playlist', required=False)
    
    # if the url arg is provided, then download the video
    if parser.parse_args().url:
        choice1(parser.parse_args().url)
    
    # if the path arg is provided, then set the path
    if parser.parse_args().path:
        savePath(parser.parse_args().path)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # if no arguments are passed, show the splash screen
    clear_screen()
    show_splash()
    print('1. Download video')
    print('2. Default Download Location')
    print('3. Download Playlist')
    print('4. Exit')
    
    choice = input('Enter your choice: ')
    if choice == '1':
        choice1()
    elif choice == '2':
        savePath()
        main()
    elif choice == '3':
        url = input('Enter the playlist url : ')
        while check_url(url) is None:
            url = input('Enter the playlist url : ')
        savedPath = read_save_path()
        save_path = savedPath if savedPath != '' else savePath()
        download_playlist(url, save_path)
    elif choice == '4':
        print('Exiting...')
        exit(0)



if __name__ == '__main__':
    main()