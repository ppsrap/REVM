import logging

import requests

from gotoassist.setting import Auth_token_input
from gotoassist.transToServiceMap import servicesName_id_map

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# https://deskapi.gotoassist.com/v1/changes/99799  return a json data

def getChangeById(changeId):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': Auth_token_input
    }

    url = "https://deskapi.gotoassist.com/v1/changes/" + str(changeId)
    response = requests.get(url, headers=headers)
    logging.info("we get：" + response.text)

def getChangeByServiceId(serviceName):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': Auth_token_input
    }

    service_id = servicesName_id_map.get(serviceName)
    url = "https://deskapi.gotoassist.com/v1/changes?service_ids=" + str(service_id)
    response = requests.get(url, headers=headers)
    logging.info("we get：" + response.text)

if __name__ == '__main__':
    # getChangeById(99799)
    getChangeByServiceId('Smartshares - Test Service')