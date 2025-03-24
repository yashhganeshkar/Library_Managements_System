import random
from decimal import Decimal
from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from datetime import date
from app.models import AdminUser, Books  # Replace 'app' with your actual app name

class Command(BaseCommand):
    help = 'Creates sample data for Library Management System'

    def handle(self, *args, **kwargs):
        # Create or get superuser
        admin = AdminUser.objects.filter(username='yash').first()
        if not admin:
            admin = AdminUser.objects.create_superuser(
                username='yash', email='yashganeshkar007@gmail.com', password='ganeshkar123'
            )
            self.stdout.write(self.style.SUCCESS(f"Created Admin: {admin.email}"))

        # Create books
        book = [
            Books(title="The Great Gatsby", author="F. Scott Fitzgerald", isbn="9780743273565", publish_date=date(1925, 4, 10), added_by=admin),
            Books(title="To Kill a Mockingbird", author="Harper Lee", isbn="9780061120084", publish_date=date(1960, 7, 11), added_by=admin),
            Books(title="1984", author="George Orwell", isbn="9780451524935", publish_date=date(1949, 6, 8), added_by=admin),
            Books(title="Moby-Dick", author="Herman Melville", isbn="9781503280786", publish_date=date(1851, 11, 14), added_by=admin),
            Books(title="Pride and Prejudice", author="Jane Austen", isbn="9781503290563", publish_date=date(1813, 1, 28), added_by=admin),
        ]

        # Bulk create books & fetch from DB
        Books.objects.bulk_create(book)
        books = Books.objects.all()
        self.stdout.write(self.style.SUCCESS(f"Inserted {len(books)} books."))


        self.stdout.write(self.style.SUCCESS("Database populated successfully!"))
