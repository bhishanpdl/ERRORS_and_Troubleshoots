# Good Resources
- [pip install --trusted-host and requests examples](https://bobbyhadz.com/blog/python-connection-error-ssl-certificate-verify-failed)

# Pip install error
```bash
# To set parameters to pip config
pip config set global.trusted-host "pypi.python.org pypi.org files.pythonhosted.org" --trusted-host=pypi.python.org --trusted-host=pypi.org --trusted-host=files.pythonhosted.org

# saves to:  C:\Users\a126291\AppData\Roaming\pip\pip.ini
```

# Request verify=False monkey patch
```python
# we should always use verify=cafile (or verify=False) instead of using this monkey patch
import requests.api
import warnings


def requestspatch(method, url, **kwargs):
    kwargs['verify'] = False
    return _origcall(method, url, **kwargs)

_origcall = requests.api.request
requests.api.request = requestspatch
warnings.warn('Patched requests: SSL verification disabled!')
```

# Requests disable SSL monkey patch
```python
import requests

session = requests.Session()
session.verify = False

requests.sessions.Session = lambda: session
```

# SSL Certification Error
```python
import os
import requests
import pandas as pd
import io

# add the certificate
certificate_path = "certificates/caadmin.netskope.com"
os.environ["REQUESTS_CA_BUNDLE"] = certificate_path

# get the data
url = "https://raw.githubusercontent.com/unit8co/darts/master/datasets/AirPassengers.csv"
response = requests.get(url)

if response.status_code == 200:
    data = response.content
    df = pd.read_csv(io.StringIO(data.decode('utf-8')))
    print(df.head())
else:
    print("Failed to download the data. Status code:", response.status_code)
```

# Encoding error
```python
Error:
UnicodeDecodeError: 'utf-8' codec can't decode     byte 0xff in position 0: invalid start byte

Troubleshoot:
df = pd.read_csv('market_share.txt',sep=r'\s+',encoding='utf-16')

# errors = ignore will remove some unparsed character that we dont care.
with open(infile, encoding='utf-16',errors='ignore') as fi:
    text = fi.readlines()
```
