# challenge_alert_notifications
Repo to solve the technical challenge received from an important real state firm.


## Get started
### Set up the environment
To execute the application you should clone the repo:
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
pip3 install requirements.txt
```

### Try the code
Execute the code:
```
python3 -m main
```

## Testing
Execute:
```
python3 -m pytest -rA
```

### Find test coverage
Run:
```
coverage run -m pytest -rA
coverage report
```

## Future work
* Define security layer (who can use the API and their permissions)
* Observability is also pending to address
* Models could be better defined, for example to validate custom and critical fields like phone number.
