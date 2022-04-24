1. Create virtualenv.
example: python3 -m venv env-name

2. Activate it.

3. Go to the project folder
```sh
cd path/to/flask-test-project
```
3. Install requirement packages:
```sh
pip install -r requirements.txt
```

4. Create db:
```sh
(venv) $ python
>>> from app import db
>>> db.create_all()
```

Run app command:
```sh
python app.py
```

Run tests example command:
```sh
pipenv run mamba tests/test_route_create.py
```
