# Booking
The application basically an online booking system that users can be booking any kind of room, hotel, etc.

#### Instruction to run the application in your local dev server:

###### Prerequisites
- Python 3.8.5
- Psql 13.0

> The following steps will walk you thru installation on a Mac. I think linux should be similar. It's also possible to develop on a Windows machine, but I have not documented the steps. If you've developed django apps on Windows, you should have little problem getting up and running.

```
git clone https://github.com/mbrsagor/booking.git
cd booking
virtualenv venv --python=python3.8
source venv/bin/activate
pip install -r requirements.txt
```

Then create ``.env`` file and paste code from `sample.env` file and add validate information.

###### Run development server:

```
python manage.py makemigrations user
python manage.py migrate user
python manage.py migrate
python manage.py runserver
```
