import os
import urllib
import requests


class OTlolls(object):
    proxies = {
        'http': 'http://127.0.0.1:8002',
        'https': 'http://127.0.0.1:8002',
    }
    headers = {
        "Host": "175.178.73.5",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "http://175.178.73.5",
        "Referer": "http://175.178.73.5/FRKToHDckx.php/category/add?dialog=1",
        "Accept-Encoding": "gzip",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Cookie": "PHPSESSID=0sdi7p2jgqo8n365oduq1bdk4l; kt_aside_menu_wrapperst=0; ACG-SHOP=jdipjerscruvj23i1vn4mu90is; df2c4333db1404e7c5cf4df435bc20f9=6b005e72-6d9b-4d3e-97f0-aa602417b553.w_oZPy-jdAN5WUyO6bavBvwX3Iw; order=id%20desc; serverType=nginx; bt_user_info=%7B%22status%22%3Atrue%2C%22msg%22%3A%22%u83B7%u53D6%u6210%u529F%21%22%2C%22data%22%3A%7B%22username%22%3A%22176****8754%22%7D%7D; pro_end=-1; ltd_end=-1; memSize=1998; sites_path=/www/wwwroot; site_model=php; db_page_model=mysql; backup_path=/www/backup; PHPSESSID=7nd3afuhtqbsudurdvtvkppn50",
        "Connection": "keep-alive",
        "Postman-Token": "df8b9bb7-b0b4-498f-a592-f67a23587b51",
    }

    @classmethod
    def add(cls, type, name, version, app_url, size,
            status, img_url="http://175.178.73.5/uploads/20230625/05c3665020f5785f325905e1ef8bf40f.jpg",
            ):
        """
        添加源
        :param type: 源分类 游戏--2 -> string
        :param name: 源名字 -> string
        :param version: 版本 -> string
        :param img_url: icon -> string
        :param app_url: app url -> string
        :param size: app size -> string
        :param status: app status 隐藏 -- hidden 上线 -- normal -> string
        :return: None
        """
        url = "http://175.178.73.5/FRKToHDckx.php/category/add?dialog=1"
        data = {
            "row[type]": type,
            "row[pid]": "0",
            "row[name]": name,
            "row[nickname]": version,
            "row[image]": img_url,
            "row[keywords]": "",
            "row[weigh]": "0",
            "row[bt1a]": app_url,
            "row[flag]": "0",
            "row[bt1b]": "",
            "row[bt2a]": size,
            "row[bt2b]": "1",
            "row[beizhu]": "",
            "row[status]": status
        }
        data = urllib.parse.urlencode(data)
        res = requests.post(url=url, headers=cls.headers, data=data, proxies=cls.proxies, verify=False)
        print(res.status_code)
        if res.status_code == 200:
            print(res.json())

    @classmethod
    def download_app(cls):
        with open("../other_source/qingtian/app_info.txt", mode="r", encoding="utf-8") as f:
            for line in f.readlines():
                line_dict = eval(line)
                if line_dict["name"][-3:] == "ipa" and line_dict["name"] not in [i.name for i in
                                                                                 os.scandir("./sources")]:
                    print(line_dict)
                    with urllib.request.urlopen(line_dict["raw_url"]) as response, open(
                            "./sources/" + line_dict["name"], "wb") as f:
                        chunk_size = 8192
                        while True:
                            chunk = response.read(chunk_size)
                            if not chunk:
                                break
                            f.write(chunk)
            # add(line_dict["name"][:-4], "1.0.0", "http://175.178.73.5/uploads/20230625/05c3665020f5785f325905e1ef8bf40f.jpg",
            #     quote(line_dict["raw_url"]), str(round(line_dict["size"] / 1024 / 1024, 2)))

    @classmethod
    def get_list(cls):
        """
        获取源list
        :return: list
        """
        url = "http://175.178.73.5/FRKToHDckx.php/category/index"
        res = requests.get(url=url, headers=cls.headers, proxies=cls.proxies, verify=False)
        print(res.status_code)
        if res.status_code == 200:
            return res.json()["rows"]
        return None

    @classmethod
    def del_o(cls, id):
        """
        删除源
        :param id:
        :return:
        """
        url = "http://175.178.73.5/FRKToHDckx.php/category/del/ids/" + id
        body = "action=del&ids={0}&params=".format(id)
        res = requests.post(headers=cls.headers, url=url, data=body, proxies=cls.proxies, verify=False)
        return res
