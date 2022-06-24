from project import check_url, download_video, read_save_path, save_path_to_file


def test_check_url():
    assert check_url(
        'https://www.youtube.com/watch?v=CdNKGrKNA6Y') == 'https://www.youtube.com/watch?v=CdNKGrKNA6Y'
    assert check_url('https://youtu.be/CdNKGrKNA6Y') == 'https://youtu.be/CdNKGrKNA6Y'
    assert check_url('') is None
    assert check_url('gychvjftyghfgchynfgyhn') is None
    

def test_save_path_to_file():
    save_path_to_file('/home/user/Downloads')
    assert read_save_path() == '/home/user/Downloads'
    save_path_to_file(path='/home/user/Desktop')
    assert read_save_path() == '/home/user/Desktop'