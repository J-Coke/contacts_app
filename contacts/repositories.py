from contacts.models import Contact


class ContactRepository:
    def create(self, contact):
        contact.save()
        return contact

    def get_all(self):
        return Contact.objects.all()