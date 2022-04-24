from expects import be_callable, equal, expect, have_property
from mamba import description, it
from mockito import mock, when

from app import Order, OrderRepository, db

with description('Test OrderRepository') as self:
    with it('has an order creation method'):
        expect(OrderRepository).to(have_property('create') & be_callable)

    with it('can create an order and return expected result'):
        expected_result = None
        order = Order(name='Sweeney Todd', address='Fleet Street, 29')
        when(db.session).add(order).thenReturn(mock(expected_result))

        result = OrderRepository(storage=db).create(order)

        expect(result).to(equal(expected_result))
