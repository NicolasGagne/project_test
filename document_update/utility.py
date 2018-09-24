# utility function

import os
import sys
import time
from document_update.const import URL_CHROMEDRIVER
import zipfile
import io

import requests

def wait_download_finish(dir):

    time.sleep(2)
    while True:
        if any(".crdownload" in s for s in os.listdir(dir)):
            time.sleep(1)
        else:
            break


def time_sleep_counter(seconds):

    for i in range(seconds):
        sys.stdout.write("\r" + 'Please Wait ' + str(seconds - i) + ' sec.')
        time.sleep(1)

    print()

def download_chromedriver(temp_dir):

    print('Downloading chromedriver.zip...')
    zip=requests.get(URL_CHROMEDRIVER).content
    zip_file = zipfile.ZipFile(io.BytesIO(zip))
    zip_file.extractall(temp_dir)
    print('Chrome driver install finish')
