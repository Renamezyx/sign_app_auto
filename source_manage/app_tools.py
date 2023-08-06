"""
    Author: Therzyx
    Email: 2274466264@qq.com
    Date: 2023/8/1$
"""
import os
import plistlib
import shutil
import zipfile

import requests


class AppTools(object):
    def __init__(self, app_url, source_path):
        """
        :param app_url: app的下载路径
        :param source_path: 下载存放目录
        :param icon_name: icon name
        """
        self.app_url = app_url
        self.source_path = source_path
        self.icon_name_patt = ["icon", "icon1", "Icon", "Icon1", "Icon72", "icon72", "Icon1024", "icon1024",
                               "Icon60@2x",
                               "icon60@2x", "AppIcon", "AppIcon60x60@2x"]
        self.app_path = None
        self.app_slist_path = None

    def _app_download(self):
        chunk_size = 1024 * 1024  # 每次下载的块大小（1MB）
        response = requests.get(self.app_url, stream=True)
        if response.status_code == 200:
            with open(os.path.join(self.source_path, "demo.ipa"), 'wb') as file:
                for chunk in response.iter_content(chunk_size=chunk_size):
                    file.write(chunk)
            print("文件下载完成")
            return os.path.join(self.source_path, "demo.ipa")
        else:
            print("文件下载失败", response)
            return None

    def _app_icon_find(self, path):
        self.app_slist_path = os.path.join(path, "Payload", os.listdir(os.path.join(path, "Payload"))[0])
        for icon_name in self.icon_name_patt:
            _icon_name_abspath = os.path.abspath(os.path.join(self.app_slist_path, icon_name + ".png"))
            if os.path.exists(_icon_name_abspath):
                return _icon_name_abspath
        return None

    def generate_icon(self):
        # 下载app
        self.app_path = self._app_download()
        if self.app_path is not None:
            # 改成zip文件
            shutil.move(self.app_path, self.app_path[:-4] + ".zip")
            # 解压
            with zipfile.ZipFile(self.app_path[:-4] + ".zip", 'r') as zip_ref:
                zip_ref.extractall(self.app_path[:-4])
            return self._app_icon_find(self.app_path[:-4])
        return None

    def get_app_info(self):
        """
        获取app_info
        :return: dict
        """
        info_list_path = os.path.join(os.path.abspath(self.app_slist_path), "Info.plist")
        with open(info_list_path, 'rb') as fp:
            plist_data = plistlib.load(fp)

        # 提取应用程序的显示名称和版本号
        display_name = plist_data.get('CFBundleDisplayName', '')
        version = plist_data.get('CFBundleShortVersionString', '')
        return {"display_name": display_name, "version": version}

    def update_zfy_welcome(self, welcome_path):
        shutil.copy(welcome_path, os.path.join(os.path.abspath(self.app_slist_path), "ZFYWelcome.plist"))

    def to_zip_to_app(self, app_name):
        new_app_path = shutil.make_archive(app_name, "zip", os.path.dirname(os.path.dirname(os.path.abspath(self.app_slist_path))))
        return shutil.move(new_app_path, "../../source/" + app_name + ".ipa")

    def clear_source(self, path):
        shutil.rmtree(os.path.abspath(path))
