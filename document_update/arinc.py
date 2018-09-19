import requests

from document_update.const import *

arinc_session = requests.Session()

arinc_session.get(ARINC_LOGIN)

arinc_session.post(ARINC_LOGIN, data=ARINC_CREDIENTIAL)

url = "https://direct.arinc.net/ADC/ADCContext/Pdf?managedDoc=2145737"
arinc_session.get("https://direct.arinc.net/ADC/ADCContext/NewCreateFPL")

pdf = arinc_session.get(url)

with open("C:/Users/ngagne/Documents/Python/project_test/document_update/" + "TEST" + ".pdf", 'wb') as doc:
    doc.write(pdf.content)


