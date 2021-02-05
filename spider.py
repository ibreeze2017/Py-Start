import json

from core import spilder, util, db
from urllib.error import HTTPError, URLError
from helper import file
import urljoin
import re
import time

data_path = "data/"
cache_path = data_path + "cache/"

# _root = 'www.netbian.com'
_root = 'desk.zol.com.cn/'
_base_url = 'http://' + _root

__filename = util.get_hash(_root)

cache_page_path = cache_path + "pages/" + __filename + "/"
cache_link_path = cache_path + "links/" + __filename + "/"
image_path = data_path + "images/" + __filename + "/"
task_path = data_path + "task/" + __filename + "/"

util.check_dirs((cache_link_path, cache_page_path, task_path))
DB = db.DB()

dstUrl = 'http://' + _root + '/'
next_set = set()
global_list = []
history_list = []
start_time = time.time()
next_list = list(next_set)
next_task = set()


def task_exist():
    return file.exist(task_path + "task-exec-" + util.get_hash(__filename) + ".tsk")


def read_task():
    # _list_exec = json.loads(file.read(task_path + "task-exec-" + util.get_hash(__filename) + ".tsk"))
    _list_set = json.loads(file.read(task_path + "task-set-" + util.get_hash(__filename) + ".tsk"))
    _list_his = json.loads(file.read(task_path + "task-history-" + __filename + ".tsk"))
    history_list.extend(_list_his)
    next_set.update(_list_set)
    next_task.update(next_set - set(history_list))


if task_exist():
    read_task()
else:
    next_set.add(dstUrl)
    next_task.update(next_set - set(history_list))

spider = spilder.Spider()

__count = 0
__max_page__ = 100
__image_list = []


def save_to_db():
    global __count
    for img in __image_list:
        img_url = img[0]
        print(str(img_url).strip())
        if str(img_url).strip() == "":
            continue
        img_alt = img[1]
        patt = re.compile("t_s\d+x\d+c\d", re.IGNORECASE)
        img_url = re.sub(patt, 't_s1920x1080c5', img_url)
        DB.insert("vx_image", {
            "url": img_url,
            "alt": img_alt,
        }).execute()
    print("本次数量：%d 张" % len(__image_list))
    __image_list.clear()
    __count = 0


def crawl(_dst_url: str):
    global __count
    history_list.append(_dst_url)
    __count = __count + 1
    filename = util.get_hash(_dst_url)
    cache_html_path = cache_page_path + filename + ".html"
    if file.exist(cache_html_path):
        html = file.read(cache_html_path)
        print("缓存读取----->" + filename)
    else:
        print("请求网络----->" + filename)
        html = spider.get_html(_dst_url)
        file.write(cache_html_path, html)
    links = spider.get_links(html)
    img_list = spider.get_img(html)
    # print(img_list)

    __image_list.extend(img_list)

    json_str = json.dumps(img_list, ensure_ascii=False)

    file.write(cache_link_path + filename + ".json", json_str)

    global_list.extend(links)

    global_set = set(global_list)

    new_set = set()

    for x in global_set:
        v = str(x).split("#")[0]
        if _root in v:
            new_set.add(v)
        else:
            if str(v).find('http') == -1:
                new_set.add(urljoin.url_path_join(_base_url, v))

    return new_set


print(next_set)


def store():
    file.write(task_path + "task-exec-" + util.get_hash(__filename) + ".tsk",
               json.dumps(list(next_task), ensure_ascii=False))
    file.write(task_path + "task-set-" + util.get_hash(__filename) + ".tsk",
               json.dumps(list(next_set), ensure_ascii=False))
    file.write(task_path + "task-history-" + __filename + ".tsk", json.dumps(history_list, ensure_ascii=False))


while len(next_task) > 0:
    next_url = next_task.pop()
    try:
        print("正在抓取：%s" % next_url)
        print("-------------------------------")
        time.sleep(0.02)
        next_set.update(crawl(next_url))
        next_task.update(next_set - set(history_list))
        print("-------------------------------")
        print("剩余链接数量：%d" % len(next_task))
    except HTTPError:
        print("HTTPError 出错了...." + next_url)
        store()
    except URLError:
        print("URLError 出错了...." + next_url)
        store()
    except ValueError:
        print("ValueError 出错了...." + next_url)
        store()
    else:
        if __count >= __max_page__:
            print("存储数据...")
            store()
            save_to_db()
            print("自动保存成功!")
else:
    used_time = time.time() - start_time
    print("执行完成！！, 耗时 %ds" % used_time)
