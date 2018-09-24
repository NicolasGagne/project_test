

from document_update.const import ARINC_CREDIENTIAL, ARINC_LOGIN_URL, ARINC_DOC_URL
from document_update.utility import time_sleep_counter

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException, NoSuchElementException

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time, os

from document_update.utility import wait_download_finish

class Arinc():
    def __init__(self, temp_dir_dict, username, password):
        self.temp_dir_dict = temp_dir_dict
        self.driver = self.create_driver()
        self.username = username
        self.password = password

        self.login()

        self.replace_aips_in_aip_folder()
        self.replace_cfss_in_cfs_folder()
        self.replace_aa_in_ops_folder()
        self.replace_aim_in_ops_folder()
        self.driver.quit()

    def create_driver(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("prefs", {"download.default_directory": self.temp_dir_dict['temp_dir'],
                                                         "download.prompt_for_download": False,
                                                         "download.directory_upgrade": True,
                                                         "safebrowsing.enabled": True
                                                         })
        driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=self.temp_dir_dict["temp_dir"] + '/chromedriver.exe')
        driver.minimize_window()
        return driver

    def login(self):
        print('Arinc Login')
        self.driver.get(ARINC_LOGIN_URL)
        self.driver.find_element_by_id("username").send_keys(self.username)
        self.driver.find_element_by_id("password").send_keys(self.password)
        self.driver.find_element_by_id("submitButton").click()
        WebDriverWait(self.driver, 10).until(EC.title_contains("Create FPL"))

    def acces_doc_page(self):
        print('Accessing Document Page')
        self.driver.get(ARINC_DOC_URL)
        WebDriverWait(self.driver, 10).until(EC.title_contains("iPad"))
        time_sleep_counter(5)

    def acces_aip_folder(self):
        self.acces_doc_page()
        print('Accessing AIP Folder')
        try:
            self.driver.find_element_by_id('ResultsContainer').\
                find_element_by_id("folder_ViewButton_1646169").click()
        except NoSuchElementException:
            self.driver.find_element_by_id('ResultsContainer'). \
                find_element_by_id("folder_ViewButton_1668551").click()

        time_sleep_counter(5)

    def acces_cfs_folder(self):
        self.acces_doc_page()
        print('Accessing CFS Folder')
        try:
            self.driver.find_element_by_id('ResultsContainer').\
                find_element_by_id("folder_ViewButton_1574769").click()
        except NoSuchElementException:
            self.driver.find_element_by_id('ResultsContainer'). \
                find_element_by_id("folder_ViewButton_1668552").click()

        time_sleep_counter(5)

    def acces_ops_folder(self):
        self.acces_doc_page()
        print('Accessing Operation Folder'),
        try:
            self.driver.find_element_by_id('ResultsContainer').\
            find_element_by_id("folder_ViewButton_1574768").click()
        except NoSuchElementException:
            self.driver.find_element_by_id('ResultsContainer'). \
                find_element_by_id("folder_ViewButton_1668554").click()

        time_sleep_counter(5)

    def delete_elements_folder(self):
        # this methode musb only be call when in actual folder.
        print('Deleting Element in this folder...')
        element_list = self.driver.find_element_by_id('ResultsContainer').find_elements_by_xpath("//*[starts-with(@id,'document_DeleteButton_')]")
        for element in element_list:
            element.click()
            try:
                self.driver.switch_to.alert.accept()
            except NoAlertPresentException as e:
                print("no alert")

        print(len(element_list), element_list)
        print('All elements have been deleted.')

    def upload_doc(self, directory):

        for root, dirs, files in os.walk(directory):
            for file in files:
                print("Uploading the following document:", os.path.join(root, file))
                self.driver.find_element_by_id('documentPane') \
                    .find_element_by_name('qqfile') \
                    .send_keys(os.path.join(root, file))
                time_sleep_counter(5)
                try:
                    self.driver.switch_to.alert.accept()
                    print("Alert")
                except NoAlertPresentException as e:
                    pass


    def replace_cfss_in_cfs_folder(self):
        self.acces_cfs_folder()
        self.delete_elements_folder()
        self.upload_doc(self.temp_dir_dict['cfs_dir'])
        time_sleep_counter(300)


    def replace_aips_in_aip_folder(self):
        self.acces_aip_folder()
        self.delete_elements_folder()
        self.upload_doc(self.temp_dir_dict['aip_dir'])
        time_sleep_counter(90)

    def replace_aa_in_ops_folder(self):
        self.acces_ops_folder()
        ## missing delete document
        self.upload_doc(self.temp_dir_dict['aa_dir'])
        time_sleep_counter(15)

    def replace_aim_in_ops_folder(self):
        self.acces_ops_folder()
        ## missing delete document
        self.upload_doc(self.temp_dir_dict['aim_dir'])
        time_sleep_counter(45)


