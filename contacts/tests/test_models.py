import pytest

from contacts.models import Contact


@pytest.mark.django_db
def test_create_contact():
    contact = Contact.objects.create(
        name="John Doe",
        address="123 Street",
        phone="555-1234",
        email="john@example.com"
    )
    assert contact.name == "John Doe"
    assert contact.address == "123 Street"
    assert contact.phone == "555-1234"
    assert contact.email == "john@example.com"