import datetime
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)


class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300), nullable=False)
    address = db.Column(db.String(300), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.datetime.utcnow)


class OrderForm(FlaskForm):
    name = StringField('name', validators=[InputRequired()])
    address = StringField('address', validators=[InputRequired()])


class DefaultResponses:
    success = "<h1>Success</h1>"
    failed = "<h1>Failed</h1>"


class OrderRepository:

    def __init__(self, storage=db):
        self.storage = storage

    def create(self, order: Order):
        self.storage.session.add(order)
        self.storage.session.commit()


class OrderController:

    def __init__(self, repository):
        self.repository = repository

    def create_order(self, order: Order):
        """
        Create an order and can contain other business logic.

        :param order: The order to be created
        """
        self.repository.create(order)


@app.route("/create", methods=['POST'])
def create():
    form = OrderForm()
    if form.validate():
        order = Order()
        form.populate_obj(order)
        order_controller = OrderController(
            repository=OrderRepository()
        )
        order_controller.create_order(order)
        return DefaultResponses.success
    else:
        return DefaultResponses.failed


if __name__ == '__main__':
    app.run()
