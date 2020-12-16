# Introduction

This is a script to help you fix your rotki DB if something happened and intervention is required.

You can either use the script (which also required you to install python 3.7 and the script's requirements) or use sqlcipher directly. In either case sqlcipher v4 needs to be installed for your OS.

# Using sqlcipher directly

This is the steps to follow to use sqlcipher and fix the db manually.

## Get sqlcipher v4

Follow the guide per your OS to get sqlcipher v4: https://rotki.readthedocs.io/en/latest/installation_guide.html#build-from-source

## Find your user's database

If you are in windows the directory should be: `%LOCALAPPDATA%/rotki/data/USERNAME` or ``%APPDATA%/rotki/data/USERNAME`

If you are in OSX the directory should be: `~/Library/Application Support/rotki/data/USERNAME`

If you are in Linux the directory should be `~/.local/share/rotki/data/USERNAME`

where `USERNAME` is the name of your rotki user.

In that directory there should be a `rotkehlchen.db`

## Access it

If you have succesfully installed sqlcipher then you can just access the DB with it. So `sqlcipher ~/.local/share/rotki/data/USERNAME/rotkehlchen.db` for Linux. For other OSes use the path that corresponds to your OS as per the previous section.

This should drop you in a DB prompt looking like this:

```
SQLite version 3.33.0 2020-08-14 13:23:32 (SQLCipher 4.4.2 community)                                                                   
Enter ".help" for usage hints. 
sqlite>
```

## Unlock it and input commands

First think you do is unlock the DB. The DB is encrypted with your user's password. So what you do is write: `PRAGMA key="YOURPASSWORD";` , where `YOURPASSWORD` is your password and press ENTER.

And now that your DB is unlocked input the following one by one:

`DROP TABLE IF EXISTS eth2_deposits;` and press ENTER
`DELETE from used_query_ranges WHERE name LIKE "eth2_deposits_%";` and press ENTER
`INSERT OR REPLACE INTO settings(name, value) VALUES('version', '22');` and press ENTER

Now you are done. This was it. Press Ctrl + D multple times to get out of the prompt and open Rotki. It should now work.


# Script Installation and running

IF you want to use the script to fix the DB these are the steps to follow

## Get sqlcipher v4

Follow the guide per your OS to get sqlcipher v4: https://rotki.readthedocs.io/en/latest/installation_guide.html#build-from-source

## Create a python 3.7 virtual env

Create a python 3.7 venv, again from the same guide: https://rotki.readthedocs.io/en/latest/installation_guide.html#build-from-source

## Install requirements

```
pip install -r requirements.txt
```

## Run the script

```
python main.py --user YOURUSERNAME --password YOURPASSWORD
```

If you also have somehow specified a custom location for rotki data then you will need to also set it with an extra argument `--data-dir /path/to/your/rotki/data/dir/`.
