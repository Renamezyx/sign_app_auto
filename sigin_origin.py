import json
import os
import urllib

import requests
from urllib.parse import quote

proxies = {
    'http': 'http://127.0.0.1:8002',
    'https': 'http://127.0.0.1:8002',
}
headers = {
    "Host": "175.178.73.5",
    "Content-Length": "537",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "http://175.178.73.5",
    "Referer": "http://175.178.73.5/FRKToHDckx.php/category/add?dialog=1",
    "Accept-Encoding": "gzip",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cookie": "dbbb53ab9bc23c86db3e661ebfb2e00e=31621997-cc3d-4323-b448-87b81f090c17.B5xJSE33ArkygP5SsWl1sF_WfaA; order=id%20desc; serverType=nginx; pro_end=-1; ltd_end=-1; bt_user_info=%7B%22status%22%3Atrue%2C%22msg%22%3A%22%u83B7%u53D6%u6210%u529F%21%22%2C%22data%22%3A%7B%22username%22%3A%22176****8754%22%7D%7D; memSize=1998; db_page_model=mysql; backup_path=/www/backup; ACG-SHOP=opebt4tqbjdhkni62bdqo3q8rt; sites_path=/www/wwwroot; site_model=php; rank=list; file_recycle_status=true; Path=/www/wwwroot/175.178.73.5/public; PHPSESSID=tmmlu6veg62q725t29kk9786h1",
    "Connection": "keep-alive"
}


def add(name, version, img_url, app_url, size):
    url = "http://175.178.73.5/FRKToHDckx.php/category/add?dialog=1"
    data = "row[type]=default" \
           "&row[pid]=0" \
           "&row[name]={0}" \
           "&row[nickname]={1}" \
           "&row[image]={2}" \
           "&row[keywords]=" \
           "&row[weigh]=0" \
           "&row[bt1a]={3}" \
           "&row[flag]=0" \
           "&row[bt1b]=" \
           "&row[bt2a]={4}" \
           "&row[bt2b]=1" \
           "&row[beizhu]=" \
           "&row[status]=hidden".format(name, version, img_url, app_url, size)
    res = requests.post(url=url, headers=headers, data=data.encode("utf-8"), proxies=proxies, verify=False)
    print(res.status_code)
    if res.status_code == 200:
        print(res.json())


with open("./raw_url.txt", mode="r", encoding="utf-8") as f:
    for line in f.readlines():
        line_dict = eval(line)
        if line_dict["name"][-3:] == "ipa" and line_dict["name"] not in [i.name for i in os.scandir("./sources")]:
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
