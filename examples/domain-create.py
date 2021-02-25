#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from hostinet.api import api

api = api(
  key = 'KEY',
  secret = 'TOKEN'
)

response = api->post("domain/create", {
    'domain':'yourdomaintoregister.com',
    'admin':'CONTACT1-HOSTI',
    'tech':'CONTACT1-HOSTI',
    'billing':'CONTACT1-HOSTI',
    'registrant':'CONTACT1-HOSTI',
    'dns1':'dns1.hostinet.com',
    'dns2':'dns2.hostinet.com',
    'years':'1',
});

print(response);
