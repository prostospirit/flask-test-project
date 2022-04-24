from expects import expect, equal
from mamba import description, it
from mockito import ANY, when, mock

import app
from app import Order, OrderController
from app import app as test_app

test_app.config['WTF_CSRF_ENABLED'] = False

with description('Test create_order called from route /create') as self:

    when(OrderController).create_order(ANY(Order)).thenReturn(mock(None))

    with it('can return failed response on incorrect (incomplete) request data'):
        with test_app.test_client() as client:
            incomplete_order = Order(name='Peter')
            response = client.post('/create', data=dict(name=incomplete_order.name))
            expect(response.data.decode()).to(equal(app.DefaultResponses.failed))

    with it('can return success response on correct request data'):
        with test_app.test_client() as client:
            order_data = dict(name='Sweeney Todd', address='Fleet Street, 29')
            response = client.post('/create', data=order_data)
            expect(response.data.decode()).to(equal(app.DefaultResponses.success))
