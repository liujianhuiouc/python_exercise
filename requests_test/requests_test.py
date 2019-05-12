
# -*- coding: utf-8 -*-

import requests

if __name__ == '__main__':
    TEA_ADMIN_URL = 'https://data.bytedance.net/tea/tea-admin/api/v2/config/app/'
    app_id = 6
    params = {'caller': 'tea_admin', 'accessed': '1', 'project_id': app_id, 'filter_keys': 'app_type'}
    response = requests.get(TEA_ADMIN_URL, params=params)
    resp_json = response.json()

    data = {key: value for key, value in resp_json['data'].items()}

    print(type(data))

    for key, value in resp_json['data'].items():
        print("key {} value {}".format(key, value['app_type']))