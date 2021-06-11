## Ansible Modules Search Utility  

Just a little bit of scraping to quickly get what you need.  
I find it quicker than ansible-doc.
I hope it will be useful.


- install python3 (possibly use a venv)  
- install requests, nuitka and bs4 (possibly use pip)  
- generate the executable for your *nix (if you need)
```
python -m nuitka list_modules.py
```
- sudo cp list_modules.bin /usr/bin/ansible_modules

USAGE:
```
ansible_modules keyword
```

### To my "likes request" collegues says: 

_"manco gli youtuber so cosi disperati giufus"_ - A.C. - Senior Middleware Developer  
  
_"se vi volete compra una foto mia, la trovate qui: `https://www.***.com/Menu/Request-a-print`"_ - M.M. - Middleware Developer  
