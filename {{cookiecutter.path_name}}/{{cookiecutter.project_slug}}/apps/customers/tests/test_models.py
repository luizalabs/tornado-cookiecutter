import pytest

from contrib.db import session

from apps.customers.models import Customer


@pytest.mark.gen_test
def test_customer_create(db):
    customer = Customer(name='Matheus Oliveira')
    customer.save()

    assert customer.id == 1


@pytest.mark.gen_test
def test_customer_delete(db):
    customer = Customer(name='Matheus Oliveira').save()
    customer.delete()

    assert session.query(Customer).get(customer.id) is None
