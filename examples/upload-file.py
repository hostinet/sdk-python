#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from hostinet.api import api

api = api(
  key = 'HOSTINET_API_KEY',
  secret = 'HOSTINET_API_SECRET'
)
list = api.post('tool/idnconverter', {
  'domain' : 'ño.com'
})

print(list)
