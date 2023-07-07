import os

import requests

headers = {
    "host": "alist.jiejingfan.vip",
    "content-length": "115",
    "pragma": "no-cache",
    "cache-control": "no-cache",
    "sec-ch-ua": "\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Google Chrome\";v=\"114\"",
    "accept": "application/json, text/plain, */*",
    "content-type": "application/json;charset=UTF-8",
    "sec-ch-ua-mobile": "?0",
    "authorization": "",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "sec-ch-ua-platform": "\"Windows\"",
    "origin": "https://alist.jiejingfan.vip",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://alist.jiejingfan.vip/%E5%AD%A6%E4%B9%A0%E8%BD%AF%E4%BB%B6/%E4%B8%80%E4%B8%AAone/%E6%88%90%E4%BA%BA%E7%89%88one%EF%BC%88%E5%85%AC%E4%BC%97%E5%8F%B7%E6%8D%B7%E5%BE%84%E8%8C%83%E5%9B%9E%E5%A4%8Done%E8%8E%B7%E5%8F%96%E5%8F%A3%E4%BB%A4%EF%BC%891.0.1.ipa",
    "accept-encoding": "gzip",
    "accept-language": "zh-CN,zh;q=0.9"
}
proxies = {
    'http': 'http://127.0.0.1:8002',
    'https': 'http://127.0.0.1:8002',
}


def get_app_url(path):
    url = "https://alist.jiejingfan.vip/api/fs/get"

    data = {"path": "/" + path, "password": ""}

    res = requests.post(url=url, headers=headers, json=data, proxies=proxies, verify=False)
    print(res.status_code)
    if res.status_code == 200 and res.json()["code"] == 200:
        res_data = res.json()["data"]
        print(res_data["name"])
        print(res_data["size"])
        print(res_data["raw_url"])
        return {"name": res_data["name"], "size": res_data["size"], "raw_url": res_data["raw_url"]}


def get_parameter_path(path=[]):
    url = "https://alist.jiejingfan.vip/api/fs/list"
    abs_paths = ["ios游戏"]
    for abs_path in abs_paths:
        json = {"path": "/" + abs_path, "password": "", "page": 1, "per_page": 50, "refresh": False}
        res = requests.post(url, json, proxies, verify=False)
        if res.status_code == 200 and res.json()["code"] == 200:
            res_data_arr = list(res.json()["data"]["content"])
            path_arr = [abs_path + "/" + i["name"] for i in res_data_arr if i["type"] == 0]
            father_path = [i["name"] for i in res_data_arr if i["type"] == 1]
            path = path_arr + path
            # 二级目录
            for f_path in father_path:
                json = {"path": "/" + abs_path + "/" + f_path, "password": "", "page": 1, "per_page": 50,
                        "refresh": False}
                res = requests.post(url=url, headers=headers, json=json, proxies=proxies, verify=False)
                if res.status_code == 200 and res.json()["code"] == 200:
                    try:
                        res_data_arr = list(res.json()["data"]["content"])
                        if len(res_data_arr) != 0:
                            path_arr = [abs_path + "/" + f_path + "/" + (i["name"]) for i in res_data_arr if
                                        i["type"] == 0]
                            other_path = [(i["name"]) for i in res_data_arr if i["type"] != 0]
                        path = path_arr + path
                    except Exception as e:
                        pass

    print(len(path))
    return path


os.remove('./raw_url.txt')
with open("./raw_url.txt", mode="w+", encoding="utf-8") as f:
    raw_urls = get_parameter_path()
    for i in raw_urls:
        f.write(str(get_app_url(i)) + "\n")
