## Ansible Modules Search Utility  

Just a little bit of scraping to quickly get what you need.  
I find it quicker than ansible-doc.
I hope it will be useful.

- build dependencies: `python3`, `requests`, `nuitka` and `bs4`  
- generate the executable 
```
python -m nuitka list_modules.py
```
- sudo cp list_modules.bin /usr/bin/ansible-modules

USAGE:
```
ansible-modules keyword
```
