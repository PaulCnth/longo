import re
import urllib3
from bs4 import BeautifulSoup as BS

# scratch web substract


class Spider():
    '''
    spider for web page's abstract
    '''

    def get_content(self, url):

        data = dict()

        headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
        http = urllib3.PoolManager()
        req = http.request(method='get', url=url, headers=headers)
        c = req.data
        s = BS(c)

        # title
        # title = ''.join(str(s.html.head.title.string).split())
        title = s.html.title.string

        # abstract, fetch the longest item
        length = [len(x.getText()) for x in s('p')]
        result = re.sub("<.*?>", "", str(s('p')[length.index(max(length))]))
        tips = ''.join(result[:300].split())

        data['title'] = title
        data['tips'] = tips

        return data
