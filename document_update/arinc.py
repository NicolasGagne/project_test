'''import requests

from document_update.const import *

arinc_session = requests.Session()

arinc_session.get(ARINC_LOGIN)

arinc_session.post(ARINC_LOGIN, data=ARINC_CREDIENTIAL)

url = "https://direct.arinc.net/ADC/ADCContext/Pdf?managedDoc=2145737"
arinc_session.get("https://direct.arinc.net/ADC/ADCContext/NewCreateFPL")

pdf = arinc_session.get(url)

with open("C:/Users/ngagne/Documents/Python/project_test/document_update/" + "TEST" + ".pdf", 'wb') as doc:
    doc.write(pdf.content)
'''

from document_update.const import ARINC_CREDIENTIAL, ARINC_LOGIN_URL, ARINC_DOC_URL

from selenium import webdriver

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

from document_update.utility import wait_download_finish

class Arinc():
    def __init__(self, temp_dir):
        self.temp_dir = temp_dir
        self.driver = self.create_driver()
        self.login()
        self.acces_aip_folder()
        self.delete_element_folder()
        self.acces_cfs_folder()
        self.delete_element_folder()



    def create_driver(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("prefs", {"download.default_directory": self.temp_dir,
                                                         "download.prompt_for_download": False,
                                                         "download.directory_upgrade": True,
                                                         "safebrowsing.enabled": True
                                                         })
        driver = webdriver.Chrome(chrome_options=chrome_options)
        driver.minimize_window()
        return driver

    def login(self):
        print('Arinc Login')
        self.driver.get(ARINC_LOGIN_URL)
        self.driver.find_element_by_id("username").send_keys(ARINC_CREDIENTIAL["username"])
        self.driver.find_element_by_id("password").send_keys(ARINC_CREDIENTIAL["password"])
        self.driver.find_element_by_id("submitButton").click()
        WebDriverWait(self.driver, 10).until(EC.title_contains("Create FPL"))


    def acces_doc_page(self):
        print('Accessing Document Page')
        self.driver.get(ARINC_DOC_URL)
        WebDriverWait(self.driver, 10).until(EC.title_contains("iPad"))
        time.sleep(5)



    def acces_aip_folder(self):
        self.acces_doc_page()
        print('Accessing AIP Folder')
        self.driver.find_element_by_id('ResultsContainer').\
            find_element_by_id("folder_ViewButton_1646169").click()
        time.sleep(3)

    def acces_cfs_folder(self):
        self.acces_doc_page()
        print('Accessing CFS Folder')
        self.driver.find_element_by_id('ResultsContainer').\
            find_element_by_id("folder_ViewButton_1574769").click()
        time.sleep(3)

    def delete_element_folder(self):
        # this methode musb only be call when in actual folder.
        print('Deleting Element in this folder...')
        element_list = self.driver.find_element_by_id('ResultsContainer').find_elements_by_xpath("//*[starts-with(@id,'document_DeleteButton_')]")


        print(len(element_list), element_list)
        print('All elements have been deleted.')