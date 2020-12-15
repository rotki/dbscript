# Installation

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


