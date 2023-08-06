from source_manage.app_tools import AppTools

source_path = "../other_source/qingtian/source_app"
get_icon = AppTools(
    "https://download4.caiyun.feixin.10086.cn:443/storageWeb/servlet/downloadServlet?code=S0gwNTExZjI2ZmkwcEM5MTIxN3R5d2tFTXU5&un=09CEA6BB65C9CD23038E6ADD0F71B892D6F259DF7F47D503A55F3D59473F009E&dom=D973&rate=0&txType=0",
    source_path, "天天")
print(get_icon.generate_icon())
