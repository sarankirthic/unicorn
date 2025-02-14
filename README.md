# unicorn
Hospital patient database

This project uses flask and postgresql

## Installation

### Create a virtual environment

```virtualenv venv -p /path/to/python/version```

### Create a postgres database and populate

```dropdb postgres1; createdb postgres1; flask db init; flask db migrate; flask db upgrade```

### To run the app

```flask run```

## API Endpoints

### ```/register```

To register user
Sending a POST request to the /register endpoint using postman 
with email and password as json data will create a new user

### ```/login```

For user login
sending a POST request to the /login endpoint using postman 
with email and password as json data will successfully login the user 

### ```/patients```

For adding patient record
Sending a POST request to the /patients endpoint using postman 
with name and patient as json data will create a new patient record 

### ```/patients/patient_id```

For retrieving patient record for that particular id
Sending a GET request to the /patients endpoint using postman and 
passing id of the patient along with the url will fetch the record 

### ```/heart_rate```

For adding patient heart rate for particular patient
Sending a POST request with the bpm and patient id will add record 
to the database

### ```/heart_rate/patient_id```
For retrieving patient bpm for particular id
Sending a GET request to the /heart_rate endpoint using postman and 
passing id of the patient along with the url will fetch the record
