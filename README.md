List Ansible Modules Utility

- install python3 (possibly use a venv)  
- install requests, nuitka and bs4 (possibly use pip)  
- generate the executable for your *nix (if you need)
```
python -m nuitka list_modules.py
```
- sudo cp list_modules.bin /usr/bin/ansible_modules
- ansible_modules keyword
