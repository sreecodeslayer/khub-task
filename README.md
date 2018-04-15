# khub-task

## Installations:
1. Setup a python environment say `.env` and install the requirements

```bash
$ pip install -r requirements.txt
```

## Run:
##### Feeding data into MongoDB
1. Head over to folder: `json`
2. Run the two scripts (Requires MongoDB installation v3.4.* or higher)

```bash
$ python script_price_tables.py
$ python commodities.py
```
> If you have auth enabled Mongo, please use the `--uri 'mongodb://<user>:<password>@<host>:<port>'` uri scheme for both scripts, defaults to `'mongodb://localhost:27017'`

##### Serving the API
1. Head back to root folder
2. Serve the API over gunicorn
> If you have auth enabled Mongo, please change the [host](https://github.com/sreecodeslayer/khub-task/blob/master/agmapi/__init__.py#L12) before serving gunicorn, default is `'mongodb://localhost:27017/AGMAPI'`

```bash
$ gunicorn --bind 0.0.0.0 --reload run:app --log-level=debug
```
