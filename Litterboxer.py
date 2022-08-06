import os
import sys
import requests
import pyperclip
import zipfile
import shutil


#If program was opened by doubleclicking
if(len(sys.argv)==1):
    print("Did you double click the file?")
    temp = input("Failed, Press ENTER to exit!")
    exit()

#Blacklisted exts by catbox
blacklist = [".exe",".jar",".doc",".docx",".cpl",".scr"]
ext = os.path.splitext(sys.argv[1])[1]

#upload expirations time
time="24h"
if os.path.exists(os.path.dirname(sys.argv[0])+"\Litterboxer.conf"):
    with open(os.path.dirname(sys.argv[0])+"\Litterboxer.conf",'r') as file:
        time=file.read().rstrip()
print("Expiration time:"+time)


try:
    #if a folder is to be uploaded, zip it
    if os.path.isdir(sys.argv[1]):
        print("Given path is a directory, proceeding to upload as zip")
        shutil.make_archive(sys.argv[1],'zip',sys.argv[1])
        #Check if folder is > 1GB
        if os.path.getsize(sys.argv[1]+".zip")>1073741824:
            print("Only files less than 1GB are allowed")
            temp = input("Failed, Press ENTER to exit!")
            exit()
        apidata={
            'time':(None,time),
            'reqtype': (None, 'fileupload'),
            'fileToUpload': (sys.argv[1]+".zip", open(sys.argv[1]+".zip", 'rb')),
        }
    #If file with blacklisted ext is to be uploaded, zip it
    elif ext in blacklist:
        #Check if filesize>1GB
        if os.path.getsize(sys.argv[1])>1073741824:
            print("Only files less than 1GB are allowed")
            temp = input("Failed, Press ENTER to exit!")
            exit()
        print("Given filetype not allowed by Catbox, so proceeding to zip and upload")
        with zipfile.ZipFile(os.path.basename(sys.argv[1])[:-4]+".zip", 'w') as zip:
            zip.write(os.path.basename(sys.argv[1]))
        apidata={
            'time':(None,time),
            'reqtype': (None, 'fileupload'),
            'fileToUpload': (sys.argv[1][:-4]+".zip", open(sys.argv[1][:-4]+".zip", 'rb')),
        }
    else:
        #Check if filesize>1GB
        if os.path.getsize(sys.argv[1])>1073741824:
            print("Only files less than 1GB are allowed")
            temp = input("Failed, Press ENTER to exit!")
            exit()
        apidata={
            'time':(None,time),
            'reqtype': (None, 'fileupload'),
            'fileToUpload': (sys.argv[1], open(sys.argv[1], 'rb')),
        }

    print("Uploading...")
    result = requests.post('https://litterbox.catbox.moe/resources/internals/api.php', files=apidata).content.decode("utf-8")
    print(result)
    pyperclip.copy(result)
    spam = pyperclip.paste()
    temp = input("Copied to Clipboard, Press ENTER to exit!")
    
except Exception as e:
    print(e)
    temp = input("Failed, Press ENTER to exit!")