#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from hostinet.api import api

api = api(
  key = 'HOSTINET_API_KEY',
  secret = 'HOSTINET_API_SECRET'
)

response = api.post("contact/create", {
  'address':'Your address',
  'city':'Your city',
  'province':'Your province',
  'postal_code':'Your postal code',
  'country':'Your country',
  'phone':'Your phone number',
  'company':'Your company',
  'email':'Your email address',
  'vat':'Your VAT',
  'first_name':'Your Name',
  'last_name':'Your Surname',
});

print(response);
