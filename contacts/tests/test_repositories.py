import pytest
from contacts.models import Contact
from contacts.repositories import ContactRepository
#


@pytest.fixture
def contact_repository():
    return ContactRepository()


@pytest.mark.django_db
def test_create_contact(contact_repository):
    contact = Contact(name="John Smith", address="123 This Street", phone="07123456789", email="john@example.com")

    created_contact = contact_repository.create(contact)

    stored_contact = Contact.objects.get(id=created_contact.id)

    assert stored_contact.name == "John Smith"
    assert stored_contact.address == "123 This Street"
    assert stored_contact.phone == "07123456789"
    assert stored_contact.email == "john@example.com"
