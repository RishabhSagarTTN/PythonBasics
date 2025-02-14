import base64
a="ZGFoaWRzYQ0Kc2FkYmhzZGYNCg=="
nlinedecode=base64.b64decode(a).decode('utf-8')
print(nlinedecode)
nlinelist= nlinedecode.splitlines()
nline = len(nlinelist)
