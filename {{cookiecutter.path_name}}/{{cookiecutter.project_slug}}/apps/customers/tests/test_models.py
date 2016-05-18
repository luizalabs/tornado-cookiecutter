import pytest

from apps.customers.models import Customer


@pytest.mark.gen_test
def test_customer_create(db):
    customer = Customer(name='Matheus Oliveira')
    customer.save()
    assert customer.id == 1
