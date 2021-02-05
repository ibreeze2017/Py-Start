import re
from urllib import request


class Spider:
    @staticmethod
    def _download(url):
        res = request.urlopen(url)
        content = str(res.read().decode('gbk'))
        return content

    def get_html(self, link):
        return self._download(link)

    def get_links(self, content):
        return self.catch_data(content, 'href="([^\'\"\(\)\{\}\[\]]+?)"')

    def get_img(self, content):
        pattern = '<img\s+(?:id=.+?)src=[\'\"]([^\'\"=\]\[\(\)]+?)[\'\"]\s*(?:title|alt=[\'\"](.+?)[\'\"])?(?:.*?)\/?>'
        return self.catch_data(content, pattern)

    @staticmethod
    def catch_data(content, regex):
        pattern = re.compile(regex, re.RegexFlag.IGNORECASE)
        data = re.findall(pattern, content)
        return data
