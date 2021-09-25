This is a Django Project.
For this you need to install Django.
Command: pip3 install django
After this comes to root directory.
And run the command given below.
python3 manage.py runserver


#Read
You might not run this with browser if you do not give any json data with request.
In order to run this you have to Install POSTMAN or use onlive version.

And send the request http://127.0.0.1:8000/
with GET method. In request body give json as given below exapmle.

{
    "sensor_id": 1,
    "model": "WS-0004",
    "payload": " asd "
}