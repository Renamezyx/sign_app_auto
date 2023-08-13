import pymysql


class MysqlBase(object):
    def __init__(self, host='175.178.73.5',
                 user='root',
                 password='6f4c219eeb4088d8',
                 database='sign_app',
                 charset='utf8mb4',
                 cursorclass=pymysql.cursors.DictCursor):
        # 建立数据库连接
        self.connection = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            charset=charset,  # 可选项，指定字符集
            cursorclass=cursorclass  # 可选项，返回字典类型的游标对象
        )

    def __del__(self):
        self.connection.close()

    def select(self, sql_str: str) -> dict:
        # 查询
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql_str)
            res = cursor.fetchall()
        except Exception as e:
            print(f"Error occurred: {str(e)}")
            res = {}
        finally:
            if cursor:
                cursor.close()
            return res

    def update(self, sql_str: str) -> int:
        # 修改
        try:
            cursor = self.connection.cursor()
            res = cursor.execute(sql_str)
        except Exception as e:
            print(f"Error occurred: {str(e)}")
            res = -1
        finally:
            if cursor:
                cursor.close()
            return res

    def delete(self, sql_str: str) -> int:
        # 删除
        try:
            cursor = self.connection.cursor()
            res = cursor.execute(sql_str)
        except Exception as e:
            print(f"Error occurred: {str(e)}")
            res = -1
        finally:
            if cursor:
                cursor.close()
            return res

    def insert(self, sql_str: str) -> int:
        # 新增
        try:
            cursor = self.connection.cursor()
            res = cursor.execute(sql_str)
        except Exception as e:
            print(f"Error occurred: {str(e)}")
            res = -1
        finally:
            if cursor:
                cursor.close()
            return res


if __name__ == '__main__':
    mysql_tools = MysqlBase()
    query = "SELECT * FROM fa_category"
    for i in mysql_tools.select(query):
        print(i)
