# Apache domain manager
Intreface for interacting with apache site configs.  
Working only on Linux.  
You must to use ```sudo```.


## Commands:
### Create:
Creates domain folder with index file, apache config file, enables config, adds information in hosts file.
```
$ python3 adm create yourdomain.com
```

### Remove:
Removes apache config link, apache config file and domain folder(if exists).
```
$ python3 adm remove yourdomain.com
```

### Ls:
Shows list of domains from ```APACHE_SITE_CONFIGS_DIR``` except files in ```LS_IGNORED_CONFIGS``` .
```
$ python3 adm ls
```

Check ```constants.py``` file to configure application.
