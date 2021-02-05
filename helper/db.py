import pymysql


class DBHelper:

    @staticmethod
    def connect(**config):
        return pymysql.Connect(**config)

