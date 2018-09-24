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


def create_list_input(session):
    responce = session.get(URL_TSA_INT)
    print(responce)

    soup = BeautifulSoup(responce.text, features="lxml")
    id_list = list()
    for input in soup.find_all("input"):
        try:
            print(input.__dict__['attrs']['id'])
            id_list.append(input.__dict__['attrs']['id'])
        except:
            pass

    print(len(id_list))
        #id_list.append(input.__dict__["id"])

def create_new_waiver(session):

    responce = session.get(URL_TSA_INT)
    print(responce)

    soup = BeautifulSoup(responce.text, features="lxml")
    print(soup.find_all("input").id)