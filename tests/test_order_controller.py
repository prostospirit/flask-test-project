from expects import be_callable, equal, expect, have_property
from mamba import description, it
from mockito import mock, when

from app import Order, OrderController, OrderRepository

with description('Test OrderController') as self:
    with it('has an order creation method'):
        expect(OrderController).to(have_property('create_order') & be_callable)

    with it('returns None when the create_order method is called when an order is passed to it'):
        expected_result = None
        order = Order(name='Sweeney Todd', address='Fleet Street, 29')
        when(OrderRepository).create(order).thenReturn(mock(expected_result))

        result = OrderController(repository=OrderRepository()).create_order(order)

        expect(result).to(equal(expected_result))
