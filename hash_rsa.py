
from rsa import sign, newkeys
import hashlib
import json


ok, ck = newkeys(64)
# print(ok.e, ok.n)
ok_e = 65537
ok_n = 13803477786977214143
# ok (e, n)
ok = str(ok_e) + ' ' + str(ok_n)
data = {'OK': ok,
        'code': 0,
        'phone': '+79515204457'}
data = json.dumps(data, sort_keys=True)
data = data.encode()
h = hashlib.sha256(data).hexdigest()
print(h)
print(data)

s = sign(data, ck, h)
s
