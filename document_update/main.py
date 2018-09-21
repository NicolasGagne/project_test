
from document_update.nav_canada_selenium import download_cfs
from document_update.nav_canada import download_aip, download_aa, download_aim
from document_update.const import *
from document_update.arinc import Arinc
import os, shutil

base_dir_path = os.path.dirname(os.path.realpath(__file__))




if __name__ == "__main__":

    temp_dir = base_dir_path + "/temp"
    try:
        os.mkdir(temp_dir)
    except FileExistsError:
        pass
    #download_cfs(temp_dir)
    #download_aip(AIP_URL, temp_dir)
    #download_aim(AIM_URL, temp_dir)
    #download_aa(AA_URL, temp_dir)
    Arinc(temp_dir)


    # remove the temp file
    #shutil.rmtree(temp_dir)
