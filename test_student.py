"""Add your two tests here. Keep the supplied baseline and smoke tests intact."""
import unittest
from models import Booking
from service import move_booking


class StudentMoveTests(unittest.TestCase):
    # Given: Existing bookings ID17, Room 201, 10-11am.
    # When: move the booking to the same room and time.
    # Expect: the booking is moved successfully without any conflicts.
    def test_unchanged_move_succeeds_without_self_conflict(self):
        target = Booking(17, "Room 201", 600, 660)
        bookings = [target]

        result = move_booking(bookings, 17, "Room 201", 600, 660)

        self.assertIs(result, target)
        self.assertEqual(bookings, [Booking(17, "Room 201", 600, 660)])



    # Given: Existing bookings ID17, Room 201, 10-11am.
    # When: move the booking to the same room and a different time and overlap.
    # Expect: the booking is moved successfully without any conflicts.
    def test_same_room_overlapping_old_interval_succeeds(self):
        target = Booking(17, "Room 201", 600, 660)
        bookings = [target]

        result = move_booking(bookings, 17, "Room 201", 630, 690)

        self.assertIs(result, target)
        self.assertEqual(target, Booking(17, "Room 201", 630, 690))

if __name__ == "__main__":
    unittest.main()
