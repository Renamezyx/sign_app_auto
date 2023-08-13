import shutil

import os

# q = QTools()
# sources_path = q.get_source_path(abs_paths=["ios游戏"])
# apps_info = []
# for source_path in sources_path:
#     apps_info.append(q.get_app_info(path=source_path))
# q.save_app_info(apps_info, path="./app_info.txt")
# 获取YY源列表
# yy_o_list = OTlolls.get_list()
# yy_o_list_info = [(i["name"], str(i["id"])) for i in yy_o_list]
# source_path = "./source_app"
# with open("app_info.txt", mode="r", encoding="utf-8") as f:
#     for line in f.readlines():
#         line_dict = eval(line)
#         if line_dict["name"][-3:] == "ipa":
#             print(line_dict)
#
#             #             for i in yy_o_list_info:
#             #                 if line_dict["name"][:-4].strip() == i[0].strip():
#             #                     OTlolls.del_o(i[1])
#             #             OTlolls.add("2", line_dict["name"][:-4], "1.0.0", line_dict["raw_url"],
#             #                         str(round(line_dict["size"] / 1024 / 1024, 2)),
#             #                         "normal")
#             #             time.sleep(1)
#             try:
#                 if not os.path.exists(os.path.abspath(source_path)):
#                     os.mkdir(os.path.abspath(source_path))
#                 app_tools = AppTools(line_dict["raw_url"], source_path)
#                 app_icon_path = app_tools.generate_icon()
#                 app_info = app_tools.get_app_info()
#                 shutil.move(os.path.abspath(app_icon_path),
#                             os.path.join("../../icon", app_info["display_name"] + "_" + app_info["version"] + ".png"))
#                 app_tools.update_zfy_welcome("./ZFYWelcome.plist")
#                 app_tools.update_zfy_icon1("./icon1.png")
#                 app_tools.to_zip_to_app(app_info["display_name"] + "_" + app_info["version"])
#                 app_tools.clear_source("./source_app")
#             except Exception as e:
#                 print(e)
#
# 去重
# apps = [{"name":i.name.split("_")[0],"version":i.name.split("_")[1][:-4],"path":i.path} for i in os.scandir("../../sources")]
# max_version_apps = {}
# print(len(apps))
# for app in apps:
#     name = app['name']
#     version = app['version']
#     path = app['path']
#
#     if name in max_version_apps:
#         if version > max_version_apps[name]['version']:
#             print(max_version_apps[name]["path"])
#             os.remove(max_version_apps[name]["path"])
#             max_version_apps[name] = {'version': version, 'path': path}
#         else:
#             print(path)
#             os.remove(path)
#     else:
#         max_version_apps[name] = {'version': version, 'path': path}
#
# result = [{'name': name, 'version': data['version'], 'path': data['path']} for name, data in max_version_apps.items()]
# print(len(max_version_apps))
# 生成文件夹和说明文件
# apps = [{"app_name": i.name, "path": i.path} for i in
#         os.scandir("../../sources") if i.name != ".DS_Store"]
# for app in apps:
#     for i in os.scandir(app["path"]):
#         cmd = "touch '" + os.path.join(os.path.abspath(app["path"]), i.name[:-4] + ".txt'")
#         os.system(cmd)

# 敏感字符过滤
replace_list = ["/", "*", "?", ":", "<", ">", "|", "\""]
apps_dir = [{"name": i.name, "path": i.path} for i in
            os.scandir(os.path.abspath("../../sources")) if i.name != ".DS_Store"]
# 文件
for i in apps_dir:
    new_dir = i["name"]
    for file in os.scandir(i["path"]):
        new_name = file.name
        for replace in replace_list:
            if file.name.find(replace) != -1:
                new_name = file.name.replace(replace, "-")
        shutil.move(file.path, os.path.join(os.path.dirname(file.path), new_name))
    # 文件夹
    for replace in replace_list:
        if i["name"].find(replace) != -1:
            new_name = i["name"].replace(replace, "-")
    shutil.move(i["path"], os.path.join(os.path.dirname(i["path"]), new_dir))
