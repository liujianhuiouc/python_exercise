
# -*- coding: utf-8 -*-

import requests

if __name__ == '__main__':
    response = requests.get(TEA_ADMIN_URL, params=params)
    resp_json = response.json()

    data = {key: value for key, value in resp_json['data'].items()}

    print(type(data))

    for key, value in resp_json['data'].items():
        print("key {} value {}".format(key, value['app_type']))