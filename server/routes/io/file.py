from flask import Blueprint, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from server.models.File import File

file = Blueprint('file', __name__)

# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://wenwen:wenwen@localhost:3306/v2020')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

session = DBSession()


@file.route('/')
def api():
    return {
        "name": "File",
        "description": "This is all the api about file"
    }


@file.route('/getList')
def get_list():
    result = []
    query_list = session.query(File).all()
    i = 0
    while i < len(query_list):
        result.append(query_list[i].as_dict())
        i += 1
    print(result)
    return {
        "code": 0,
        "error": None,
        "message": "success",
        "data": result
    }
