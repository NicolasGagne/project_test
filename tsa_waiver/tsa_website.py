import requests
import json
from bs4 import BeautifulSoup


from tsa_waiver.const import *

def login_tsa_website():
    session = requests.Session()


    login_page = session.get(URL_TSA_LOGIN)


    soup = BeautifulSoup(login_page.text, features="lxml")
    csrf = soup.find(type="hidden")
    print(csrf.__dict__['attrs']['value'])
    TSA_CREDIENTIAL['i_token'] = csrf.__dict__['attrs']['value']

    session.post(URL_TSA_LOGIN, data=TSA_CREDIENTIAL)


    print(session.get("https://waivers.faa.gov/aap/te_pages.p_main"))

    return session