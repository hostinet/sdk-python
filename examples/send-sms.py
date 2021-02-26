#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from hostinet.api import api

api = api(
  key = 'HOSTINET_API_KEY',
  secret = 'HOSTINET_API_SECRET'
)

test = api.post('sms',{
  'to': '+34.123456789',
  'from': 'Sara',
  'text': 'This is a test SMS',
})

print(test)
