# Introduction
- [github repo for jq binary releases](https://github.com/jqlang/jq)
- [python module jq](https://pypi.org/project/jq/)
- [github repo for binary jq issues](https://github.com/mwilliamson/jq.py/issues/20)
- https://stackoverflow.com/questions/32911446/error-installing-jq-on-windows?rq=3

# Install python module jq on windows
1. Install `jq` binary from github releases and put in windows path. (check: `jq --version`)
2. Download the correct python version python pip wheel for windows from [https://jeffreyknockel.com/jq/](https://jeffreyknockel.com/jq/)
3. Activate the environment the install the wheel.
```
ge pai2
cd ~/Softwares/jq
# download wheel and put it here
ls # jq-1.6.0-cp312-cp312-win_amd64.whl
pip install jq-1.6.0-cp312-cp312-win_amd64.whl
```

# Testing
```python
import jq

assert jq.compile(".").input_value(None).first() == None
assert jq.compile(".").input_value(42).first() == 42
assert jq.compile(".").input_value(0.42).first() == 0.42
assert jq.compile(".").input_value(True).first() == True
assert jq.compile(".").input_value("hello").first() == "hello"
```
