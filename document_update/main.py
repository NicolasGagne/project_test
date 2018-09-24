
from document_update.nav_canada_selenium import download_cfs
from document_update.nav_canada import download_aip, download_aa, download_aim
from document_update.utility import time_sleep_counter, download_chromedriver
from document_update.const import ARINC_CREDIENTIAL, AIM_CREDIENTIAL, AIP_URL, AA_URL, AIM_URL
from document_update.arinc import Arinc
import os, shutil


base_dir_path = os.path.dirname(os.path.realpath(__file__))




if __name__ == "__main__":


    temp_dir = (base_dir_path + "/temp")

    temp_dir_dict = {
        "temp_dir": temp_dir,
        "cfs_dir": temp_dir + "/cfs",
        "aip_dir": temp_dir + "/api",
        "aa_dir": temp_dir + "/aa",
        "aim_dir": temp_dir + "/aim"
    }

    for key, value in temp_dir_dict.items():
        try:
            print("create folder: ", value)
            os.mkdir(value)
        except FileExistsError:
            print("Folder all ready exit")
    download_chromedriver(temp_dir_dict['temp_dir'])
    download_cfs(temp_dir_dict)
    download_aip(AIP_URL, temp_dir_dict['aip_dir'])
    download_aim(AIM_URL, temp_dir_dict['aim_dir'])
    download_aa(AA_URL, temp_dir_dict['aa_dir'])
    Arinc(temp_dir_dict, ARINC_CREDIENTIAL["username"], ARINC_CREDIENTIAL["password"])
    Arinc(temp_dir_dict, AIM_CREDIENTIAL["username"], AIM_CREDIENTIAL["password"])

    # remove the temp file
    print('Deleting all temp files.')
    shutil.rmtree(temp_dir)

    print("DONE You can quit")
    time_sleep_counter(300)
