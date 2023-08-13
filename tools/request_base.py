from requests import sessions
import config


class RequestBase(object):
    def __init__(self):
        self.session = sessions.Session()
        self.debug = config.DEBUG
        self.proxies = {
            'http': 'http://127.0.0.1:8002',
            'https': 'http://127.0.0.1:8002',
        }

    def request(self, method, url, **kwargs):
        if self.debug:
            return self.session.request(method=method, url=url, verify=False, proxies=self.proxies, **kwargs)
        else:
            return self.session.request(method=method, url=url)
