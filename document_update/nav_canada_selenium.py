import time
from selenium import webdriver

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def download_cfs():

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("prefs", {"download.default_directory": r"C:\Users\ngagne\Documents\Python\project_test\document_update",
                                              "download.prompt_for_download": False,
                                              "download.directory_upgrade": True,
                                              "safebrowsing.enabled": True
                                              })
    driver = webdriver.Chrome(chrome_options=chrome_options)

    NAV_CANADA_LOGIN = "https://checkout.na3.netsuite.com/c.1063417/checkout-2-05-0/index.ssp?is=login&origin=defaultbehavior&whence=#login-register"
    NAV_CANADA_DOWNLOAD_PAGE = "https://checkout.na3.netsuite.com/app/site/hosting/scriptlet.nl?script=12&deploy=1&compid=1063417&custpage_sel_lang=en_CA&whence="
    payload = {'email': "yquellais@hotmail.com", 'password': "star9025", 'redirect': "true", }
    driver.get(NAV_CANADA_LOGIN)
    driver.find_element_by_id("login-email").send_keys("yquellais@hotmail.com")
    driver.find_element_by_id('login-password').send_keys("star9025")
    driver.find_element_by_id('login-view').find_element_by_tag_name('button').click()

    WebDriverWait(driver, 10).until(EC.title_contains("Home - NetSuite Canada (NAV CANADA)"))

    driver.get(NAV_CANADA_DOWNLOAD_PAGE)
    cfs_link = driver.find_element_by_id('custpage_ns_rela_uoo_list_splits').find_elements_by_tag_name('tr')


    print("cfs_link", len(cfs_link))
    x = 0
    for link in cfs_link:
        x = x + 1
        print('link', link)

        try:
            link.find_element_by_tag_name('a').click()


        except:
            print('no working ', x)

    time.sleep(300)
