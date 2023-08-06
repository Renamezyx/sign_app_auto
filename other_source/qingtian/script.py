import json
import shutil
import time

from other_source.qingtian.q_tools import QTools
from source_manage.app_tools import AppTools
from source_manage.o_tools import OTlolls
import os

q = QTools()
sources_path = q.get_source_path(abs_paths=["ios游戏"])
apps_info = []
for source_path in sources_path:
    apps_info.append(q.get_app_info(path=source_path))
q.save_app_info(apps_info, path="./app_info.txt")
# 获取YY源列表
# yy_o_list = OTlolls.get_list()
# yy_o_list_info = [(i["name"], str(i["id"])) for i in yy_o_list]
source_path = "./source_app"
with open("app_info.txt", mode="r", encoding="utf-8") as f:
    for line in f.readlines():
        line_dict = eval(line)
        if line_dict["name"][-3:] == "ipa":
            print(line_dict)

            #             for i in yy_o_list_info:
            #                 if line_dict["name"][:-4].strip() == i[0].strip():
            #                     OTlolls.del_o(i[1])
            #             OTlolls.add("2", line_dict["name"][:-4], "1.0.0", line_dict["raw_url"],
            #                         str(round(line_dict["size"] / 1024 / 1024, 2)),
            #                         "normal")
            #             time.sleep(1)
            if not os.path.exists(os.path.abspath(source_path)):
                os.mkdir(os.path.abspath(source_path))
            app_tools = AppTools(line_dict["raw_url"],source_path)
            app_icon_path = app_tools.generate_icon()
            app_info = app_tools.get_app_info()
            shutil.move(os.path.abspath(app_icon_path),
                        os.path.join("../../icon", app_info["display_name"] + "_" + app_info["version"] + ".png"))
            app_tools.update_zfy_welcome("./ZFYWelcome.plist")
            app_tools.to_zip_to_app(app_info["display_name"] + "_" + app_info["version"])
            app_tools.clear_source("./source_app")
