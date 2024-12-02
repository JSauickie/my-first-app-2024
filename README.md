# my-first-app-2024

## Setup

Create and ctivate a virtual enviroment


```sh
conda create -n reports-env-2024 python=3.10
``` 

activate enviroment:

```sh
conda activate reports-env-2024
```



install packages:

```sh
pip install -r requirements.txt
```

[Obtain an API Key](https://www.alphavantage.co/support/#api-key) from AlphaVantage.


Create a .env file and add contents like the following(using your own alpavantage api key):

```sh
#this is the ".env file
ALPHAVANTAGE_API_KEY="..."


## Usage

Run the example script:

```sh
python app/my_script.py
```



run the unemployment report:

```sh
#ALPHAVANTAGE_API_KEY="....." python app/unemployment.py

#python app/unemployment.py
python -m app.unemployment


```


Run the stocks report:

```sh
#python app/stocks.py

python -m app.stocks
```


## Testing

Run tests:

```sh
pytest
```
###web app run

Run the web app (then view in the browser at http://localhost:5000/):

```sh
# Mac OS:
FLASK_APP=web_app flask run

# Windows OS:
# ... if `export` doesn't work for you, try `set` instead
# ... or set FLASK_APP variable via ".env" file
export FLASK_APP=web_app
flask run
```

