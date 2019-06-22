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
