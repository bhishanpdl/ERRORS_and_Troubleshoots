# Best way 01: Using downloaded certificate in environment
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

# Best way 2: Using certificate netscope.com file
```python
import requests
import os
import io

note = r'''
Open website in Chrome and click on top left lock sign
Connection is Secure > Certificate if Valid > Details > select top hierarchy > Export
and save inside folder 'certificate'

'''

certificate_path = "certificates/caadmin.netskope.com"
assert os.path.isfile(certificate_path), "File not found"

url = "https://raw.githubusercontent.com/unit8co/darts/master/datasets/AirPassengers.csv"

response = requests.get(url, verify=certificate_path)

if response.status_code == 200:
    data = response.content
    df = pd.read_csv(io.StringIO(data.decode('utf-8')))
    display(df.head())
else:
    print("Failed to download the data. Status code:", response.status_code)
```

# Bad way: requests.get and verify=False
```python
import requests
url = "https://raw.githubusercontent.com/unit8co/darts/master/datasets/AirPassengers.csv"
try:
    response = requests.get(url,verify=False)
    data_str = response.content
    print(data_str[:10])
except requests.exceptions.SSLError as e:
    print(str(e))
```

# Alternative best way: Reading file direclty using pandas
```python
import pandas as pd

url = "https://raw.githubusercontent.com/unit8co/darts/master/datasets/AirPassengers.csv"
df = pd.read_csv(url)
df.iloc[[0,1,-2,-1]]
```
