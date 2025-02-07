#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from hostinet.api import api

api = api(
  key = 'HOSTINET_API_KEY',
  secret = 'HOSTINET_API_SECRET'
)

response = api.post("tool/csrdecode", {
  'csr': '-----BEGIN CERTIFICATE REQUEST-----\
MIIC1jCCAb4CADCBkTELMAkGA1UEBhMCVVMxGzAZBgNVBAMTEmV4YW1wbGUuZG9t\
YWluLmNvbTESMBAGA1UEBxMJQ3VwZXJ0aW5vMR8wHQYDVQQKExZZb3VyIFNvbHV0\
aW9ucyBDb21wYW55MRMwEQYDVQQIEwpDYWxpZm9ybmlhMRswGQYDVQQLExJEZWZh\
dWx0IERlcGFydG1lbnQwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDF\
j0w0I74ENSBvXua62+PVz226Hkw/84RWG3bv/NRrbyyHAwP4Gn4zpCjo/dbZo5mX\
R9ZCqr4cQDCVcWohqZwfYF1auDXYRcey9ov367F+F9UmzGJq8WHDVv+o7FHk/kyc\
DY5UJXK+EuxKqsLe9nlzeTJ4fxC8P2WEIJGjePsBrAZofvMmT+3nQA5ZrWH8mXgQ\
f6FTAzxhYPjvEmo/LWq7kEGbZzsaMY6vtGTgXkd2tWDvOLw7IbTmsteV0+KSPdBj\
c1lh02DgCzcrVAUWbaA4dLNE3xytEZkB/NGlLmjnmU/Ju94RqzVNb6jSLPhgrMQY\
pPtfYXJJvbIXglHgv2cJAgMBAAGgADANBgkqhkiG9w0BAQsFAAOCAQEAegYHo0Hl\
66oBE+vlafoOzPPIsQ3oyYlDFTRUZF/f3vbpzyldWm5i7G00FO0NcFbo1EXM2KST\
ykiePZflSBupWtAQxcTRxPSLRZGGQM+PpzejKdc9rOTazeWvDKW25M/X435yr2ku\
U+htd7cdOd9hmMPGgbzETehTK7UHd10uK32bDzbwhJ/44or58MB9jAHCN7sVK77+\
JBrTpVQDIEsPiHHlZQCjoZjSZiuowb2oeQMCNuCxVlxCmpzsQRyhOBzyhKa1mF/B\
VHplaI/0Wah+mtnfiSDwGPsWy2c5qJ/8UvH7TDLxcVKzMl0A1NFp0JheqQtx3IJN\
3kRIx76M36ybFA==\
-----END CERTIFICATE REQUEST-----'
});

print(response)
