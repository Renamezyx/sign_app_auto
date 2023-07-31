import os
import shutil
import zipfile

source_apps = [i for i in os.scandir("./sources")]
for app in source_apps:
    zip_file_name = app.name[:-4] + ".zip"
    if not os.path.exists(r"C:\Users\Admin\Desktop\sign_app_auto\t"):
        os.mkdir(r"C:\Users\Admin\Desktop\sign_app_auto\t")
    shutil.move(app.path, "./t/" + zip_file_name)
    with zipfile.ZipFile("./t/" + zip_file_name, 'r') as zip_ref:
        zip_ref.extractall("./t/" + app.name[:-4])
    payload_path = os.path.join("./t", app.name[:-4], "Payload")
    icon_names = ["icon", "icon1", "Icon", "Icon1", "Icon72", "icon72", "Icon1024", "icon1024", "Icon60@2x",
                  "icon60@2x", "AppIcon", "AppIcon60x60@2x"]
    for icon_name in icon_names:
        icon_path = os.path.join(payload_path, os.listdir(payload_path)[0], icon_name + ".png")
        if os.path.exists(icon_path):
            break
    shutil.move(icon_path, os.path.join("../icon", app.name[:-4] + ".png"))
    shutil.rmtree("./t")
