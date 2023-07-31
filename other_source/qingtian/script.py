import json
import time

from other_source.qingtian.q_tools import QTools
from source_manage.o_tools import OTlolls

# q = QTools()
# sources_path = q.get_source_path(abs_paths=["ios游戏"])
# apps_info = []
# for source_path in sources_path:
#     apps_info.append(q.get_app_info(path=source_path))
# q.save_app_info(apps_info, path="app_info.txt")
# 获取YY源列表
yy_o_list = OTlolls.get_list()
yy_o_list_info = [(i["name"], str(i["id"])) for i in yy_o_list]
with open("app_info.txt", mode="r", encoding="utf-8") as f:
    for line in f.readlines():
        line_dict = eval(line)
        if line_dict["name"][-3:] == "ipa":
            print(line_dict)
            for i in yy_o_list_info:
                if line_dict["name"][:-4].strip() == i[0].strip():
                    OTlolls.del_o(i[1])
            OTlolls.add("2", line_dict["name"][:-4], "1.0.0", line_dict["raw_url"],
                        str(round(line_dict["size"] / 1024 / 1024, 2)),
                        "normal")
            time.sleep(1)
