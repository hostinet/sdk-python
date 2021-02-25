#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from hostinet.api import api

api = api(
  key = 'KEY',
  secret = 'TOKEN'
)

test = api.get('profile')

print(test)
