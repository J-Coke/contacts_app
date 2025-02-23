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


@pytest.mark.django_db
def test_get_all_contacts(contact_repository):
    # Create a couple of contacts
    contact1 = Contact.objects.create(name="Alice", address="456 Lane", phone="555-5678", email="alice@example.com")
    contact2 = Contact.objects.create(name="Bob", address="789 Road", phone="555-8765", email="bob@example.com")

    # Use the repository to fetch all contacts
    contacts = contact_repository.get_all()

    # Verify both contacts are in the result
    assert len(contacts) == 2
    assert contacts[0].name == "Alice"
    assert contacts[1].name == "Bob"