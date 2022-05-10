import requests
from bs4 import BeautifulSoup
import os
import traceback
import threading
import sys

def download(url, filename,name):
    if os.path.exists(filename):
        print('file exists!')
        return
    try:
        r = requests.get(url, stream=True, timeout=60)
        r.raise_for_status()
        with open(name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:  # filter out keep-alive new chunks
                    f.write(chunk)
                    f.flush()
        return filename
    except KeyboardInterrupt:
        if os.path.exists(filename):
            os.remove(filename)
        raise KeyboardInterrupt
    except Exception:
        traceback.print_exc()
        if os.path.exists(filename):
            os.remove(filename)


if os.path.exists('imgs') is False:
    os.makedirs('imgs')

def download_thread(start, end):

    for i in range(start, end):
        url = f'http://konachan.net/post/show/{i}'
        html = requests.get(url).text
        soup = BeautifulSoup(html, 'html.parser')
        for img in soup.find_all('img', class_="image"):
            target_url = img['src']
            filename = os.path.join('imgs', target_url.split('/')[-1])
            name = os.path.join('imgs', str(i)) + '.jpg' 
            download(target_url, filename,name)
            
            
def main(start = 1,end = 341508,thread_number = 100):
    number = (end - start)//thread_number
    warning_file = open('warning.txt','w')
    sys.stdout = warning_file
    sys.stderr = warning_file
    for id in range(thread_number):
        t = threading.Thread(target=download_thread, args=(start, start + number))
        t.start()
        start = start + number
    

if __name__ == '__main__':
    main()