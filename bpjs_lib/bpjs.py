from django.conf import settings

from urllib.parse import urljoin

from .base import Base
from .utils import generate_signature


class Vclaim(Base):

    def get_url(self):
        base_url = settings.BPJS_VCLAIM_BASE_URL
        return urljoin(base_url, self.route)

    def get_headers(self):
        message = f'{self.cons_id}&{self.timestamp}'
        signature = generate_signature(self.secret_key, message)
        headers = {
            'X-signature': signature,
            'X-cons-id': self.cons_id,
            'X-timestamp': str(self.timestamp),
            'user_key': settings.BPJS_VCLAIM_USER_KEY
        }
        return headers


class AntrianBPJS(Base):

    def get_url(self):
        base_url = settings.BPJS_ANTRIAN_RS_BASE_URL
        return urljoin(base_url, self.route)

    def get_headers(self):
        message = f'{self.cons_id}&{self.timestamp}'
        signature = generate_signature(self.secret_key, message)
        headers = {
            'X-signature': signature,
            'X-cons-id': self.cons_id,
            'X-timestamp': str(self.timestamp),
            'user_key': settings.BPJS_ANTRIAN_RS_USER_KEY
        }
        return headers







