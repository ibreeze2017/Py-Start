import conf
from helper import db, util

DBHelper = db.DBHelper
typeof = util.typeof


class DB:
    __conn = None

    __config = conf.database

    _temp_sql = ''

    @classmethod
    def get_conn(cls):
        if DB.__conn is None:
            DB.__conn = DBHelper.connect(**DB.__config)
        return DB.__conn

    def insert(self, table: str, _map: dict):
        _sql = 'insert into ' + table + ' '
        _len = len(_map.keys())
        _fields = ''
        _values = ''
        for idx, k in enumerate(_map.keys()):
            _fields = _fields + '`' + k + '`'
            if idx < _len - 1:
                _fields = _fields + ','

        for idx, k in enumerate(_map.values()):
            if typeof(k) == 'str':
                res = '\'' + k + '\''
            else:
                res = k

            _values = _values + res
            if idx < _len - 1:
                _values = _values + ','
        _sql = _sql + '(' + _fields + ') values (' + _values + ')'
        self._temp_sql = _sql
        return self

    def query(self, table: str, where: dict):
        _sql = 'select * from ' + table
        _where = ''
        _arr = []
        for k, v in where:
            _arr.append('`' + k + '`=' + ('\'' + v + '\'' if typeof(k) == 'str' else v))

        if not _where == '':
            _sql = _sql + ' where ' + ','.join(_arr)
        return self

    def fetch_all(self):
        cursor = self.execute()
        cursor.close()
        return cursor.fetchall()

    def execute(self):
        conn = DB.get_conn()
        cursor = conn.cursor()
        print(self._temp_sql)
        cursor.execute(self._temp_sql)
        conn.commit()
        return cursor

    @staticmethod
    def close():
        DB.get_conn().close()
