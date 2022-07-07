# Booking
The application basically, is an online booking system that users can be booking any kind of room, hotel, etc.

#### Instruction to run the application in your local dev server:

###### Prerequisites
- Python 3.8.5
- Psql 14.0

> The following steps will walk you thru installation on a Mac. I think linux should be similar. It's also possible to develop on a Windows machine, but I have not documented the steps. If you've developed django apps on Windows, you should have little problem getting up and running.

```
git clone https://github.com/mbrsagor/booking.git
cd booking
virtualenv venv --python=python3.8
source venv/bin/activate
pip install -r requirements.txt
```

###### Then create ``.env`` file and paste code from `sample.env` file and add validate information.

-------------------------------------------
```bash
|--> sample.env
|--> .env
```

###### Run development server:

```
python manage.py makemigrations rent
python manage.py migrate rent
python manage.py migrate
python manage.py runserver
```


###### Rest API endpoint:
```bash
http://127.0.0.1:8000/api/
```

#### psql DB new for python3.10 to 3.10
```bash
pip install psycopg2
```


###### LOGGING: project settings.py file paste the code
```python
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,                                                                    
    'handlers': {                                                                                         
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': '/code/myapp/logs/info.log',             
        },
        'console': { 
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',                                                             
        },                                                                                                
    },
    'loggers': {
        'django': {
            'handlers': ['file'],                                                                         
            'level': 'INFO',
            'propagate': True,                                                                            
        },
        'app-logger': { 
            'handlers': ['file', 'console'],                                                              
            'level': 'CRITICAL',                                                                          
            'propagate': True,                                                                            
        },                                                               
    }, 
}
```
------------------

```python
import logging

def appError():
    appLogger = logging.getLogger('app-logger')                                                           
    appLogger.critical("A critical error occurred")
```

## Happy coding :wink:
