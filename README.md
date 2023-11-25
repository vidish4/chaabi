# chaabi
Chaabi Vector DB - LLM Assignment

Download the `.zip` file from the repository and extract it in the choice of your directory. Alternatively you can also use git.<br />
Open the main folder `chaabi` from any command line. Make sure you have `python` and `pip` installed.<br />
Make a virtual environment with `python = 3.11`: <br />
```
conda create -n test python=3.11
``` 
Additional required Modules and Libaries are written in `requirements.txt`. Once in the main directory run the following command: <br />
```
pip install -r requirements.txt
```

Run the following command to check for migrations:
```
python manage.py migrate
```

If everything is okay, start the server:
```
python manage.py runserver
```

You'll be given the following link `http://127.0.0.1:8000/`. Open it in a web browser.

Enter any query related to `bigBasketProducts.csv` and the response will be generated shortly!
