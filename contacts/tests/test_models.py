import pytest
from django.db import IntegrityError

from contacts.models import Contact


@pytest.mark.django_db
def test_create_contact():
    contact = Contact(
        name="John Smith",
        address="123 This Street",
        phone="07123456789",
        email="john@example.com"
    )
    assert contact.name == "John Smith"
    assert contact.address == "123 This Street"
    assert contact.phone == "07123456789"
    assert contact.email == "john@example.com"

@pytest.mark.django_db
def test_contact_email_unique():
    contact1 = Contact(
        name="John Smith",
        address="123 This Street",
        phone="07123456789",
        email="john.smith@example.com"
    )
    contact1.full_clean()  # Ensures model-level validation
    contact1.save()

    contact2 = Contact(
        name="Jane Smith",
        address="456 Avenue",
        phone="07987654321",
        email="john.smith@example.com"
    )
    with pytest.raises(Exception):
        contact2.full_clean()
        contact2.save()