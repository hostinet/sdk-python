#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from hostinet.api import api

api = api(
  key = 'HOSTINET_API_KEY',
  secret = 'HOSTINET_API_SECRET'
)

response = api.post("profile", {
    'email': 'new@email.com',
    'email2': 'secondnew@email.com'
});
print_r(response);
