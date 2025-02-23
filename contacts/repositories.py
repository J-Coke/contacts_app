class ContactRepository:
    def create(self, contact):
        contact.save()
        return contact