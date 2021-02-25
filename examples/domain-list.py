#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from hostinet.api import api

api = api(
  key = 'KEY',
  secret = 'TOKEN'
)

response = api->get("domain/list");

print(response);

response = api->get("domain/list", {
  'limit': 10,
  'page': 2,
});

print(response);
