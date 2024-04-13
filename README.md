1. Create virtualenv
```
python -m venv [path to venv folder]
```
2. Activate virtualenv
``` 
.\venv\Scripts\activate (for Windows)
source env/bin/activate (for Linux)
```
3. Change directory
``` 
cd news_backend
```
4. Install requirements
``` 
pip install -r requirements.txt
```
5. Create db
``` 
python manage.py migrate
```
6. (Optionally) Create admin
``` 
python manage.py createsuperuser
```
7. Run server
``` 
python manage.py runserver
```
8. access swagger schema at
``` 
http://127.0.0.1:8000/swagger/#/
```
