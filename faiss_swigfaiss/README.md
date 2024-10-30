# Error
- date: 2024-09-03

References:
- https://github.com/kyamagu/faiss-wheels/issues/39

**Error**
```python
INFO:faiss.loader:Loading faiss with AVX512 support.
INFO:faiss.loader:Could not load library with AVX512 support due to:
ModuleNotFoundError("No module named 'faiss.swigfaiss_avx512'")
INFO:faiss.loader:Loading faiss with AVX2 support.
INFO:faiss.loader:Could not load library with AVX2 support due to:
ModuleNotFoundError("No module named 'faiss.swigfaiss_avx2'")

```

# Attempt
- Press win button, search "Powershell", right click and run as admin
```powershell
cd "C:\Users\a126291\AppData\Local\miniconda3\envs\py312_llama_index\Lib\site-packages\faiss"
dir # make sure you see: swigfaiss.py
New-Item -ItemType SymbolicLink -Path "swigfaiss_avx2.py" -Target "swigfaiss.py"
dir # make sure you see: swigfaiss_avx2.py
```

# Error installing faiss-cpu in py313_lang conda env
- Date: 2024-10-30
- https://anaconda.org/pytorch/faiss-cpu


**Using pip fails**
```
1. can not install using pip
$ pip install faiss-cpu==1.9.0 --force

Collecting faiss-cpu==1.9.0
  Using cached faiss_cpu-1.9.0.tar.gz (67 kB)

      building 'faiss._swigfaiss' extension
      swigging faiss\faiss\python\swigfaiss.i to faiss\faiss\python\swigfaiss_wrap.cpp
      swig.exe -python -c++ -Doverride= -doxygen -Ifaiss -IC:\Users\a126291\AppData\Local\Temp\pip-build-env-b4yixrek\overlay\Lib\site-packa
ges\numpy\_core\include -Ifaiss -I/usr/local\include -DSWIGWIN -o faiss\faiss\python\swigfaiss_wrap.cpp faiss\faiss\python\swigfaiss.i
      error: command 'swig.exe' failed: None
      [end of output]

  note: This error originates from a subprocess, and is likely not a problem with pip.
  ERROR: Failed building wheel for faiss-cpu
Failed to build faiss-cpu
ERROR: ERROR: Failed to build installable wheels for some pyproject.toml based projects (faiss-cpu)
(py313_lang)

```

**Using conda also fails**
```
 conda install pytorch::faiss-cpu==1.9.0
C:\Users\a126291\AppData\Local\miniconda3\Lib\site-packages\urllib3\connectionpool.py:1099: InsecureRequestWarning: Unverified HTTPS request
 is being made to host 'conda.anaconda.org'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/lat
est/advanced-usage.html#tls-warnings
  warnings.warn(
Channels:
 - defaults
 - pytorch
 - conda-forge
Platform: win-64
Collecting package metadata (repodata.json): done
Solving environment: | warning  libmamba Added empty dependency for problem type SOLVER_RULE_UPDATE
failed

LibMambaUnsatisfiableError: Encountered problems while solving:
  - package faiss-cpu-1.9.0-py3.10_h491596c_0_cpu requires python >=3.10,<3.11.0a0, but none of the providers can be installed

Could not solve for environment specs
The following packages are incompatible
├─ faiss-cpu 1.9.0  is installable with the potential options
│  ├─ faiss-cpu 1.9.0 would require
│  │  └─ python >=3.10,<3.11.0a0 , which can be installed;
│  ├─ faiss-cpu 1.9.0 would require
│  │  └─ python >=3.11,<3.12.0a0 , which can be installed;
│  ├─ faiss-cpu 1.9.0 would require
│  │  └─ python >=3.12,<3.13.0a0 , which can be installed;
│  └─ faiss-cpu 1.9.0 would require
│     └─ python >=3.9,<3.10.0a0 , which can be installed;
└─ pin-1 is not installable because it requires
   └─ python 3.13.* , which conflicts with any installable versions previously reported.
```
