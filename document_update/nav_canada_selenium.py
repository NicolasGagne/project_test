
from selenium import webdriver

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from document_update.utility import wait_download_finish
from document_update.const import NAV_CANADA_DOWNLOAD_PAGE, NAV_CANADA_LOGIN_URL, NAV_CANADA_CREDIENTIAL

def download_cfs(temp_dir_dict):

    chrome_options = webdriver.ChromeOptions()
    print(temp_dir_dict['temp_dir'])
    chrome_options.add_experimental_option("prefs", {"download.default_directory": temp_dir_dict['cfs_dir'],
                                              "download.prompt_for_download": False,
                                              "download.directory_upgrade": True,
                                              "safebrowsing.enabled": True
                                              })
    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=temp_dir_dict["temp_dir"] + '/chromedriver.exe')
    driver.minimize_window()

    driver.get(NAV_CANADA_LOGIN_URL)
    WebDriverWait(driver, 10).until(EC.title_contains("Sign In | Register"))
    driver.find_element_by_id("login-email").send_keys(NAV_CANADA_CREDIENTIAL["email"])
    driver.find_element_by_id('login-password').send_keys(NAV_CANADA_CREDIENTIAL["password"])
    driver.find_element_by_id('login-view').find_element_by_tag_name('button').click()

    WebDriverWait(driver, 10).until(EC.title_contains("Home - NetSuite Canada (NAV CANADA)"))

    driver.get(NAV_CANADA_DOWNLOAD_PAGE)
    cfs_link = driver.find_element_by_id('custpage_ns_rela_uoo_list_splits').find_elements_by_tag_name('tr')

    x = 0
    for link in cfs_link:
        try:
            link.find_element_by_tag_name('a').click()
            x = x + 1
        except:
            print('Link Not Working ', link)
    print(x, " CFS Downloading...")

    wait_download_finish(temp_dir_dict['cfs_dir'])

    driver.quit()
    print("CFS downloads completed.")

