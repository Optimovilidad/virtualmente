import json
import requests


class API():
    def __init__(self, env='local'):
        self.url_prod = "http://optimovilidad.com/aplications/radio/public/postradiodata"
        self.url_local = "http://localhost/optimovilidad/admin/radio/public/postradiodata"
        if env == 'local':
            self.url = self.url_local
        else:
            self.url = self.url_prod

    def send_data(self, text):
        try:
            payload = json.dumps({
                "txt": text
            })
            headers = {
                'Content-Type': 'application/json',
            }
            requests.request("POST", self.url, headers=headers, data=payload)
        except Exception:
            pass
