from project_func import check_url, green, red, blue, clear_screen, show_splash, savePath, read_save_path, download_video, download_playlist, choice1
import sys



# Youtube Offline Downloader

def main():
    # get arguments from user using argparse module
    import argparse






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