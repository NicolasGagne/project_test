

import requests


AIP_AD_ENG = "http://www.navcanada.ca/EN/products-and-services/Documents/AIP/Current/part_3_ad/3ad_eng.pdf"



AIP_URL = {
    'AIP_GEN_ENG': "http://www.navcanada.ca/EN/products-and-services/Documents/AIP/Current/part_1_gen/1gen_eng.pdf",
    'AIP_ENR_ENG':"http://www.navcanada.ca/EN/products-and-services/Documents/AIP/Current/part_2_enr/2enr_eng.pdf",
    'AIP_AD_ENG': "http://www.navcanada.ca/EN/products-and-services/Documents/AIP/Current/part_3_ad/3ad_eng.pdf",
    'AIP_SUP_ENG':"http://www.navcanada.ca/EN/products-and-services/Documents/AIP/Current/part_4_aip_sup/4aip_sup_eng.pdf",
    'AIP_AIC_ENG':"http://www.navcanada.ca/EN/products-and-services/Documents/AIP/Current/part_5_aic/5aic_eng.pdf"
    }

def download_aip():

    for key, value in AIP_URL.items():
        responce = requests.get(value)
        with open(key + '.pdf', 'wb') as file:
            file.write(responce.content)

def download_aim():
    responce = requests.get("http://www.tc.gc.ca/media/documents/ca-publications/AIM-2018-1-E-ACCESS.pdf")
    with open("Aeronautical Information Manual (AIM)" + '.pdf', 'wb') as file:
        file.write(responce.content)



def download_aa():
    responce = requests.get("http://laws-lois.justice.gc.ca/PDF/A-2.pdf")
    with open("Aeronautical Act" + '.pdf', 'wb') as file:
        file.write(responce.content)

download_aa()