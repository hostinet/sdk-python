#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from hostinet.api import api

api = api(
  key = 'HOSTINET_API_KEY',
  secret = 'HOSTINET_API_SECRET'
)

response = api.get("contact/list");

print(response);

response = api.get("contact/list", {
  'limit': 10,
  'page': 2,
});

print(response);
