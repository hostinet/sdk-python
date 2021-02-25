#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from hostinet.api import api

api = api(
  key = 'KEY',
  secret = 'TOKEN'
)

test = api.post('tool/idnconverter', {
  'domain': 'exámple.com'
})

print(test)
