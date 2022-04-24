## Task:
implement based on hexagonal architecture

mamba + expects + mocks tests for the service

Reference:

https://medium.com/@vsavkin/hexagonal-architecture-for-rails-developers-8b1fee64a613
https://en.wikipedia.org/wiki/Hexagonal_architecture_(software)
https://www.youtube.com/watch?v=tg5RFeSfBM4

## Installation

1. Go to the project folder
```sh
cd path/to/flask-test-project
```

2. Create virtualenv.
```sh
python3 -m venv env
```

3. Activate it.
```sh
source env/bin/activate
```

5. Install requirement packages:
```sh
pip install -r requirements.txt
```

4. Create db:
```sh
(venv) $ python3
>>> from app import db
>>> db.create_all()
```

## Run

Run app:
```sh
python3 app.py
```

Run tests example command:
```sh
pipenv run mamba tests/test_route_create.py
```
