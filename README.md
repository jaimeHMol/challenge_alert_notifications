# challenge_alert_notifications
Repo to solve the technical challenge received from an important real state firm.


## Get started
### Set up the environment
To execute the application (in Unix based systems) you should clone the repo:
```
git clone https://github.com/jaimeHMol/challenge_alert_notifications.git
```

Go into the new created folder and create a virtual environment:
```
cd tech-challenge
python3 -m venv venv
```

Activate the virtual environment:
```
source venv/bin/activate
```

Install the requirements:
```
pip install requirements.txt
```

### Try the app
Execute the code:
```
uvicorn alert_notifications_api.main:app --reload
```
Then, access the url: **[127.0.0.1:8000/docs](127.0.0.1:8000/docs)** to see all the documentation of the API.


## Testing
Execute:
```
python -m pytest -rA
```

### Find test coverage
Run:
```
coverage run -m pytest -rA
coverage report
```

## Architecture definition
### The production ready proposal:
#### High level architecture
![image](https://github.com/jaimeHMol/challenge_alert_notifications/assets/28209920/908d6421-ea4d-47e5-9a60-c0b550172d37)

#### API backend
![image](https://github.com/jaimeHMol/challenge_alert_notifications/assets/28209920/2ae15832-73bc-48aa-b5d8-f9d04cb5dbb6)

#### Data model
![image](https://github.com/jaimeHMol/challenge_alert_notifications/assets/28209920/6b0e7f83-43b9-4030-9d92-556eb0d3ce78)


### The mocked proposal for this challenge:
In order to limit the scope of this challenge (mainly because time availability
constraints) I have decided to implement all the blocks described in the "production
ready proposal" in a simple, plain, Python implementation just to have all the elements
running in local, tested and easily customizable (mockable).

You will find all of them here in this repo.

In terms of Python dependencies I use the minimum required subset of the dependencies
defined for the "production ready proposal". They basically are:
* FastApi (For the API Backend)
* SQLModel (For the ORM)
* Pydantic (For some model validations)



## Future work
* Define security layer (who can use the API and their permissions)
* Observability is also pending to address
* Models could be better defined, for example, validating custom and critical fields like phone number, or validating referential data between tables.
* Create the rest of the endpoints and organize them by entity using blueprints or something similar.