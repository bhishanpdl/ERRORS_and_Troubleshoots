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
- Pres win button, search "Powershell", right click and run as admin
```powershell
cd "C:\Users\a126291\AppData\Local\miniconda3\envs\py312_llama_index\Lib\site-packages\faiss"
dir # make sure you see: swigfaiss.py
New-Item -ItemType SymbolicLink -Path "swigfaiss_avx2.py" -Target "swigfaiss.py"
dir # make sure you see: swigfaiss_avx2.py
```
