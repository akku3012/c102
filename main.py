from types import TracebackType
import cv2
import dropbox
import time
import random
start_time = time.time()
def take_snapshot():
    number = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videoCaptureObject.read()
        img_name = 'img'+ str(number)+'.png'
        cv2.imwrite(img_name,frame)
        start_time = time.time
        result = False
    return img_name
    print('snapshot taken')
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_file(img_name):
    access_token = 'sl.A29KD1JKNILNcEdzUEA7bQ1JTQJgj1qjC5madhJEoctWlGIHMr6zUjcSNICc0fN6uLvyoYWfz1MLbeKhu2k89YzS15afvETINosmS1b7ZkX36YArNG30IyvITZAcotL6vKqN_dw'
    file = img_name
    file_from = file    
    file_to = '/Users/HP_BOOK_PRO/Dropbox/Users/HP_BOOK_PRO/Dropbox/testFolder/'+(img_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from,'rb') as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print('File Uploaded')

def main():
    while(True):
        if((time.time() - start_time)>=300):
            name = take_snapshot()
            upload_file(name)

main()