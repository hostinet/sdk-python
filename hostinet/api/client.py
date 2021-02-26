import requests

class client():
    url = 'https://www.hostinet.com/api/'
    uagent = 'hostinet-api v0.3-beta'
    token = None
    key = None
    secret = None
    version = 1.1

    def __init__(self, **kargs):
        self.key = kargs.get('key', None)
        self.secret = kargs.get('secret', None)
        self.token = None
        pass

    def request(self, method, url, data={}):
      json = self.http(method, url, data)
      return json

    def http(self, method, url, data):
      if(self.token is None and self.auth() is False):
        return False
      return self.connect(method, url, data)

    def connect(self, method, url, data):
      nurl = self.url + url
      if nurl[-1] != '/':
        nurl = nurl + '/'
      headers = {
        'user-agent': '{}; Platform/Python; PlatformVersion/{}'.format(self.uagent, self.version),
        'Expect': '',
      }
      if self.token is not None:
        headers['token'] = self.token

      if method == 'POST':
        x = requests.post(nurl, data=data, headers=headers)
      elif method == 'DELETE':
        x = requests.delete(nurl, data=data, headers=headers)
      elif method == 'PUT':
        x = requests.put(nurl, data=data, headers=headers)
      elif method == 'UPLOAD':
        x = requests.post(nurl, files=data, headers=headers)
      else:
        x = requests.get(nurl, params=data, headers=headers)

      try:
        json = x.json()
      except ValueError:
        return False
      return json

    def auth(self):
      if not self.key or not self.secret:
        return False
      json = self.connect('POST', 'auth', {
        'appkey':self.key,
        'appsecret':self.secret
      })
      if json is False or json['success'] is False:
        return False
      self.token = json['token']
      return True
