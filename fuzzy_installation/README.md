# fuzzy (fuzzy matching NLP module) errors
```
$ /Users/poudel/miniconda3/envs/dataSc/bin/pip install fuzzy
Collecting fuzzy
  Using cached https://files.pythonhosted.org/packages/ad/b0/210f790e81e3c9f86a740f5384c758ad6c7bc1958332cf64263a9d3cf336/Fuzzy-1.2.2.tar.gz
Building wheels for collected packages: fuzzy
  Building wheel for fuzzy (setup.py) ... error
  ERROR: Command errored out with exit status 1:
   command: /Users/poudel/miniconda3/envs/dataSc/bin/python -u -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/tb/7xdk9scs79j9hxzcl3l_s6k00000gn/T/pip-install-85s8hvxc/fuzzy/setup.py'"'"'; __file__='"'"'/private/var/folders/tb/7xdk9scs79j9hxzcl3l_s6k00000gn/T/pip-install-85s8hvxc/fuzzy/setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' bdist_wheel -d /private/var/folders/tb/7xdk9scs79j9hxzcl3l_s6k00000gn/T/pip-wheel-06u_pkrq --python-tag cp37
       cwd: /private/var/folders/tb/7xdk9scs79j9hxzcl3l_s6k00000gn/T/pip-install-85s8hvxc/fuzzy/
  Complete output (11 lines):
  running bdist_wheel
  running build
  running build_ext
  building 'fuzzy' extension
  creating build
  creating build/temp.macosx-10.9-x86_64-3.7
  creating build/temp.macosx-10.9-x86_64-3.7/src
  x86_64-apple-darwin13.4.0-clang -DNDEBUG -fwrapv -O3 -Wall -Wstrict-prototypes -march=core2 -mtune=haswell -mssse3 -ftree-vectorize -fPIC -fPIE -fstack-protector-strong -O2 -pipe -D_FORTIFY_SOURCE=2 -mmacosx-version-min=10.9 -I/Users/poudel/miniconda3/envs/dataSc/include/python3.7m -c src/fuzzy.c -o build/temp.macosx-10.9-x86_64-3.7/src/fuzzy.o
  clang-4.0: error: no such file or directory: 'src/fuzzy.c'
  clang-4.0: error: no input files
  error: command 'x86_64-apple-darwin13.4.0-clang' failed with exit status 1
  ----------------------------------------
  ERROR: Failed building wheel for fuzzy
  Running setup.py clean for fuzzy
Failed to build fuzzy
Installing collected packages: fuzzy
  Running setup.py install for fuzzy ... error
    ERROR: Command errored out with exit status 1:
     command: /Users/poudel/miniconda3/envs/dataSc/bin/python -u -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/tb/7xdk9scs79j9hxzcl3l_s6k00000gn/T/pip-install-85s8hvxc/fuzzy/setup.py'"'"'; __file__='"'"'/private/var/folders/tb/7xdk9scs79j9hxzcl3l_s6k00000gn/T/pip-install-85s8hvxc/fuzzy/setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' install --record /private/var/folders/tb/7xdk9scs79j9hxzcl3l_s6k00000gn/T/pip-record-k5lj1b0d/install-record.txt --single-version-externally-managed --compile
         cwd: /private/var/folders/tb/7xdk9scs79j9hxzcl3l_s6k00000gn/T/pip-install-85s8hvxc/fuzzy/
    Complete output (11 lines):
    running install
    running build
    running build_ext
    building 'fuzzy' extension
    creating build
    creating build/temp.macosx-10.9-x86_64-3.7
    creating build/temp.macosx-10.9-x86_64-3.7/src
    x86_64-apple-darwin13.4.0-clang -DNDEBUG -fwrapv -O3 -Wall -Wstrict-prototypes -march=core2 -mtune=haswell -mssse3 -ftree-vectorize -fPIC -fPIE -fstack-protector-strong -O2 -pipe -D_FORTIFY_SOURCE=2 -mmacosx-version-min=10.9 -I/Users/poudel/miniconda3/envs/dataSc/include/python3.7m -c src/fuzzy.c -o build/temp.macosx-10.9-x86_64-3.7/src/fuzzy.o
    clang-4.0: error: no such file or directory: 'src/fuzzy.c'
    clang-4.0: error: no input files
    error: command 'x86_64-apple-darwin13.4.0-clang' failed with exit status 1
    ----------------------------------------
ERROR: Command errored out with exit status 1: /Users/poudel/miniconda3/envs/dataSc/bin/python -u -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/tb/7xdk9scs79j9hxzcl3l_s6k00000gn/T/pip-install-85s8hvxc/fuzzy/setup.py'"'"'; __file__='"'"'/private/var/folders/tb/7xdk9scs79j9hxzcl3l_s6k00000gn/T/pip-install-85s8hvxc/fuzzy/setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' install --record /private/var/folders/tb/7xdk9scs79j9hxzcl3l_s6k00000gn/T/pip-record-k5lj1b0d/install-record.txt --single-version-externally-managed --compile Check the logs for full command output.
                                                                                                                                [ 5s544 | Sep 01 09:21AM ]
```
