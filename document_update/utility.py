# utility function

import os
import time


def wait_download_finish(dir):

    time.sleep(2)
    while True:
        if any(".crdownload" in s for s in os.listdir(dir)):
            time.sleep(1)
        else:
            break