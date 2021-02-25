from .client import client

class api():
    def __init__(self, **kargs):
        key = kargs.get('key', '')
        secret = kargs.get('secret', '')
        self.client = client(
          key=key,
          secret=secret
        )

    def get(self, url, data={}):
      return self.client.request('GET', url, data)

    def post(self, url, data={}):
      return self.client.request('POST', url, data)

    def put(self, url, data={}):
      return self.client.request('PUT', url, data)

    def delete(self, url, data={}):
      return self.client.request('DELETE', url, data)

    def upload(self, file):
      files = {'file': open(file, 'rb')}
      return self.client.request('UPLOAD', 'tool/upload', files)
      pass
