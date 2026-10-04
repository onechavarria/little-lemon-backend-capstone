from django.test import TestCase
from .models import MenuItem, Booking


class MenuItemTest(TestCase):

    def test_create_menu_item(self):
        item = MenuItem.objects.create(
            title="Greek Salad",
            price=8.50,
            inventory=20
        )

        self.assertEqual(item.title, "Greek Salad")
        self.assertEqual(float(item.price), 8.50)
        self.assertEqual(item.inventory, 20)


class BookingTest(TestCase):

    def test_create_booking(self):
        booking = Booking.objects.create(
            first_name="Alcindo",
            reservation_date="2026-10-10",
            reservation_slot=10
        )

        self.assertEqual(booking.first_name, "Alcindo")
        self.assertEqual(booking.reservation_slot, 10)
