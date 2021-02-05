

def typeof(variate):
    _type = None
    if isinstance(variate, int):
        _type = "int"
    elif isinstance(variate, str):
        _type = "str"
    elif isinstance(variate, float):
        _type = "float"
    elif isinstance(variate, list):
        _type = "list"
    elif isinstance(variate, tuple):
        _type = "tuple"
    elif isinstance(variate, dict):
        _type = "dict"
    elif isinstance(variate, set):
        _type = "set"
    return _type
