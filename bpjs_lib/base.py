from django.conf import settings

import time
import requests
from .utils import decrypt_data


class Base:

    def __init__(self,
                 route,
                 data=None,
                 json=None,
                 files=None,
                 params=None):
        self.route = route
        self.r_data = data
        self.r_json = json
        self.r_files = files
        self.r_params = params
        self.timestamp = int(round(time.time()))
        self.__resp = None

        self.cons_id = settings.BPJS_CONS_ID
        self.secret_key = settings.BPJS_SECRET_KEY

    def get_headers(self):
        raise NotImplementedError('`.get_headers()` must be implemented.')

    def get_url(self):
        raise NotImplementedError('`.get_headers()` must be implemented.')

    def get_kwargs(self):
        return {
            'data': self.r_data,
            'json': self.r_json,
            'files': self.r_files,
            'params': self.r_params,
            'headers': self.get_headers()
        }

    def __do_request(self, method, url, **kwargs):
        request = requests.request(method=method, url=url, **kwargs)
        self.__resp = request

    def get(self):
        self.__do_request(method='get', url=self.get_url(), **self.get_kwargs())

    def post(self):
        self.__do_request(method='post', url=self.get_url(), **self.get_kwargs())

    def put(self):
        self.__do_request(method='put', url=self.get_url(), **self.get_kwargs())

    def delete(self):
        self.__do_request(method='delete', url=self.get_url(), **self.get_kwargs())

    @property
    def response(self):
        if self.__resp is None:
            raise ValueError('You must call `.get()`, `.post()`, or .`put()` before access `.response`')
        return self.__resp

    @property
    def data(self):
        if self.__resp is None:
            raise ValueError('You must call `.get()`, `.post()`, or .`put()` before access `.response`')
        if not self.response.json().get('response'):
            return None
        decrypt = decrypt_data(
            cons_id=self.cons_id,
            secret_key=self.secret_key,
            timestamp=str(self.timestamp),
            data=self.response.json().get('response')
        )
        return decrypt

