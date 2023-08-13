from tools.mysql_base import MysqlBase
import time


class SQLTools(MysqlBase):
    def __init__(self):
        super().__init__()

    def add_list(self, type: int, name: str, version: str, flag: int, image: str, desc: str, status: int,
                 app_url: str, size: float) -> int:
        """
        添加记录
        :param type: app_type
        :param name: app_name
        :param version: app_version
        :param flag: 是否付费 0 or 1
        :param image: image_url
        :param desc: desc
        :param status: status normal or
        :param app_url: app_url
        :return: int
        """
        # INSERT INTO fa_category(type, name, nickname, flag, image,keywords,createtime,updatetime, status, bt1a,bt2b,bt2a)
        # VALUES(2,'app_name','version',0,'icon_url','desc',1691920072,1691920072,'normal','app_url',2)
        sql_str = r"INSERT INTO fa_category(type, name, nickname, flag, image,keywords,createtime,updatetime, status, bt1a,bt2b) " \
                  r"VALUES({0},'{1}','{2}',{3},'{4}','{5}',{8},{8},'{6}','{7}',0,{9})".format(type, name, version, flag,
                                                                                              image, desc, status,
                                                                                              app_url,
                                                                                              int(time.time()),
                                                                                              int(size * 1024 * 1024))

        print(sql_str)
        res = self.insert(sql_str)
        return res


if __name__ == '__main__':
    sql_tool = SQLTools()
    sql_tool.add_list(2, 'app_name', 'version', 0, 'icon_url', 'desc', 'normal', 'app_url', 1)
