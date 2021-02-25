#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from hostinet.api import api

api = api(
  key = 'KEY',
  secret = 'TOKEN'
)

test = api.post('sms',{
  'to': '+34.123456789',
  'from': 'Sara',
  'text': 'This is a test SMS',
})

print(test)
