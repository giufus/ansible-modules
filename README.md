## Ansible Modules Search Utility  

Just a little bit of scraping to quickly get what you need.  
I find it quicker than ansible-doc.
I hope it will be useful.

- build dependencies: `python3`, `requests`, `nuitka` and `bs4`  
- generate the executable (optional)
```
python -m nuitka list_modules.py
```

USAGE: source or binary
```
python list_modules.py <keyword>
```

```
list_modules.bin <keyword>
```
