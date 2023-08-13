"""
    Author: Therzyx
    Email: 2274466264@qq.com
    Date: 2022-07-30
"""
import os
import requests


class QTools(object):
    """
    软件源: 晴天源
    源地址: https://alist.jiejingfan.vip
    """
    # api
    urls = {"fs_list": "https://alist.jiejingfan.vip/api/fs/list",
            "fs_get": "https://alist.jiejingfan.vip/api/fs/get"}
    # 所需 headers
    headers = {
        "content-type": "application/json;charset=UTF-8",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }
    proxies = {
        'http': 'http://127.0.0.1:8002',
        'https': 'http://127.0.0.1:8002',
    }

    # api action
    def get_app_info(self, path):
        """
        获取app资源详细信息
        :param path: 目录 -> string
        :return: app资源详细信息 -> dict
        """
        json = {"path": "/" + path, "password": ""}

        res = requests.post(url=self.urls["fs_get"], headers=self.headers, json=json, proxies=self.proxies,
                            verify=False)
        print(res.status_code)
        if res.status_code == 200 and res.json()["code"] == 200:
            res_data = res.json()["data"]
            return {"name": res_data["name"], "size": res_data["size"], "raw_url": res_data["raw_url"]}

    def get_source_path(self, abs_paths=[]):
        """
        获取有app资源的目录
        :param abs_paths: 原始目录 -> []
        :return: 有app资源的目录 ->[]
        """
        path = []
        # 遍历 abs_paths,检索一级目录，获取可用资源，add到path
        for abs_path in abs_paths:
            json = {"path": "/" + abs_path, "password": "", "page": 1, "per_page": 50, "refresh": False}
            res = requests.post(headers=self.headers, url=self.urls["fs_list"], json=json, proxies=self.proxies,
                                verify=False)
            print(res.status_code)
            if res.status_code == 200 and res.json()["code"] == 200:
                res_data_arr = list(res.json()["data"]["content"])
                path_arr = [abs_path + "/" + i["name"] for i in res_data_arr if i["type"] == 0]
                father_path = [i["name"] for i in res_data_arr if i["type"] == 1]
                path = path_arr + path
                # 遍历 father_path,检索二级目录，获取可用资源，add到path
                for f_path in father_path:
                    json = {"path": "/" + abs_path + "/" + f_path, "password": "", "page": 1, "per_page": 50,
                            "refresh": False}
                    res = requests.post(headers=self.headers, url=self.urls["fs_list"], json=json, proxies=self.proxies,
                                        verify=False)
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

    def save_app_info(self, app_infos, path="app_info.txt"):
        """
        保存app_info信息
        :param app_infos: app信息 -> list
        :param path: 保存路径 -> string
        :return: None
        """
        if os.path.exists(path):
            os.remove(path)
        with open("app_info.txt", mode="w+", encoding="utf-8") as f:
            for app_info in app_infos:
                f.write(str(app_info) + "\n")


if __name__ == '__main__':
    q = QTools()
    sources_path = q.get_source_path(abs_paths=["ios游戏"])
    apps_info = []
    for source_path in sources_path:
        apps_info.append(q.get_app_info(path=source_path))
    q.save_app_info(apps_info, path="./app_info.txt")
