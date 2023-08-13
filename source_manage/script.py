from alist_tools import AListTools
from sql_tools import SQLTools

# 获取app_info
alist_tools = AListTools()
sql_tools = SQLTools
dirs = alist_tools.get_dirs("games")
apps_info = []
for dir in dirs:
    app_info = alist_tools.get_app_info(dir)
    if app_info:
        apps_info.append(app_info)
print(apps_info)

for app_info in apps_info:

    sql_tools.add_list(2, apps_info["app_name"], app_info["app_version"], 0, app_info["app_icon"], app_info["app_desc"], 'normal', app_info["app_url"], 1)