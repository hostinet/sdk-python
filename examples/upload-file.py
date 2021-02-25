#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from hostinet.api import api

api = api(
  key = '5f289661b751ec8c78',
  secret = '74c7e812bbbc5a8f75b89b464e4e35b75b4c404a17'
)
list = api.post('tool/idnconverter', {
  'domain' : 'ño.com'
})

print(list)
