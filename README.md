1. Create virtualenv
```
python -m venv [path to venv folder]
```
2. Activate virtualenv
``` 
.\venv\Scripts\activate (for Windows)
source env/bin/activate (for Linux)
```
3. Install requirements
``` 
pip install -r requirements.txt
```
5. Change directory
``` 
cd news_backend
```
6. Create db
``` 
python manage.py migrate
```
7. (Optionally) Create admin
``` 
python manage.py createsuperuser
```
8. Run server
``` 
python manage.py runserver
```
9. access swagger schema at
``` 
http://127.0.0.1:8000/swagger/#/
```
