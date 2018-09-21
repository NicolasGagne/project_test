# utility function

import os
import sys
import time

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

