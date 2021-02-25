#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from hostinet.api import api

api = api(
  key = 'KEY',
  secret = 'TOKEN'
)

response = api->post("contact/info", {
  'name': 'CONTACT1-HOSTI'
});

print(response);
