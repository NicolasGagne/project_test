

import requests
from lxml import html

# AIP (no password)



AIP_AD_ENG = "http://www.navcanada.ca/EN/products-and-services/Documents/AIP/Current/part_3_ad/3ad_eng.pdf"



AIP_URL = {
    'AIP_GEN_ENG': "http://www.navcanada.ca/EN/products-and-services/Documents/AIP/Current/part_1_gen/1gen_eng.pdf",
    'AIP_ENR_ENG':"http://www.navcanada.ca/EN/products-and-services/Documents/AIP/Current/part_2_enr/2enr_eng.pdf",
    'AIP_AD_ENG': "http://www.navcanada.ca/EN/products-and-services/Documents/AIP/Current/part_3_ad/3ad_eng.pdf",
    'AIP_SUP_ENG':"http://www.navcanada.ca/EN/products-and-services/Documents/AIP/Current/part_4_aip_sup/4aip_sup_eng.pdf",
    'AIP_AIC_ENG':"http://www.navcanada.ca/EN/products-and-services/Documents/AIP/Current/part_5_aic/5aic_eng.pdf"
    }

NAV_CANADA_LOGIN = "https://checkout.na3.netsuite.com/c.1063417/checkout-2-05-0/index.ssp"
NAV_CANADA_LOGIN1 = "https://checkout.na3.netsuite.com/c.1063417/checkout-2-05-0/index.ssp?is=login&login=T&sc=1&reset=T#login-register"
NAV_CANADA_CREDIENTIAL = {'login-email': 'yquellais@hotmail.com', 'login-password': 'star9025'}

CFS_URL = {

}
def download_aip():

    for key, value in AIP_URL.items():
        responce = requests.get(value)
        with open(key + '.pdf', 'wb') as file:
            file.write(responce.content)

def download_cfs():
    nav_canada_session = requests.Session()

    nav_canada_session.get(NAV_CANADA_LOGIN)
    nav_canada_session.post(NAV_CANADA_LOGIN, data=NAV_CANADA_CREDIENTIAL)

    page = nav_canada_session.get("https://checkout.na3.netsuite.com/app/site/hosting/scriptlet.nl?script=12&deploy=1&compid=1063417&custpage_sel_lang=en_CA&whence=")


    webpage = html.fromstring(page.content)
    print(page.text)
    print(page.headers)
    print(page.content)
    print(webpage.xpath('*'))
    print(webpage.xpath('//a/@href'))

download_cfs()