#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from hostinet.api import api

api = api(
  key = 'HOSTINET_API_KEY',
  secret = 'HOSTINET_API_SECRET'
)

# Set a IP to "www.mydomain.com"
response = api.post("domain/dyndns", {
  'ip':'xxx.xxx.xxx.xxx',
  'domain':'mydomain.com',
  'host':'www',
});

print(response);

# Set a IP to "mydomain.com"
response = api.post("domain/dyndns", {
  'ip':'xxx.xxx.xxx.xxx',
  'domain':'mydomain.com',
  'host':'@',
});

print(response);

# Set automatic IP to "mydomain.com"
response = api.post("domain/dyndns", {
  'domain':'mydomain.com',
  'host':'@',
});

print(response);
