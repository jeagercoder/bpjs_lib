

```python
#   settings.py

BPJS_CONS_ID = ''
BPJS_SECRET_KEY = ''

BPJS_VCLAIM_BASE_URL = ''
BPJS_VCLAIM_USER_KEY = ''

BPJS_ANTRIAN_RS_BASE_URL = ''
BPJS_ANTRIAN_RS_USER_KEY = ''
```

```python
from bpjs_lib.bpjs import Vclaim

#   Post data
data = {}
v = Vclaim(route='RencanaKontrol/InsertSPRI', json=data)
v.post()
v.response  # return object python requests
v.data  # return data that has been decrypt if any

#   Get data
diagnosa_code = 'A04'
route = f'referensi/diagnosa/{diagnosa_code}'
v = Vclaim(route=route)
v.get()
v.response  # return object python requests
v.data
```