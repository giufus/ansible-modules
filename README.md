List Ansible Modules Utility

- install python3 (possibly use a venv)  
- install requests, nuitka and bs4 (possibly use pip)  
- generate the executable for your *nix (if you need)
```
python -m nuitka list_modules.py
```
- sudo ln -s /usr/local/bin/ansible_modules "abs path of list_modules.bin" (if you want)
- ansible_modules | grep -A1 something
