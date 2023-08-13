from tools.request_base import RequestBase

request = RequestBase().request


class AListTools(object):
    def __init__(self):
        self.url = "http://175.178.73.5:5244"
        self.headers = {"Content-Type": "application/json;charset=UTF-8"}

    def get_dirs(self, type):
        url = self.url + "/api/fs/list"
        req_json = {"path": "/games", "password": ""}
        res = request("post", url, headers=self.headers, json=req_json)
        print(res.status_code)
        if res.status_code == 200:
            res_dict = res.json()["data"]["content"]
            # 获取一级目录
            return ["/" + type + "/" + dir_dict["name"] for dir_dict in res_dict]
        return None

    def get_app_info(self, dir):
        url = self.url + "/api/fs/list"
        req_json = {"path": dir}
        res = request("post", url, headers=self.headers, json=req_json)
        print(req_json)
        if res.status_code == 200:
            res_dict = res.json()["data"]["content"]
            for list in res_dict:
                if list["name"][-3:] == "txt":
                    desc = list["name"][:-4]
                else:
                    app_name = list["name"].split("_")[0]
                    app_version = list["name"].split("_")[1][:-4]
                    app_size = round(list["size"] / 1024 / 1024, 2)
                    app_url = url + dir + list["name"]
                    app_icon = "https://github.com/Renamezyx/sign_app_auto/blob/main/icon/" + list["name"][:-3] + "png"
            return {"app_name": app_name, "app_version": app_version, "app_size": app_size, "app_desc": desc,
                    "app_url": app_url,
                    "app_icon": app_icon}
            return None


if __name__ == '__main__':
    alist_tools = AListTools()
    dirs = alist_tools.get_dirs("games")
    apps_info = []
    for dir in dirs:
        app_info = alist_tools.get_app_info(dir)
        apps_info.append(app_info)
    print(apps_info)
