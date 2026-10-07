In service.py / move_booking, the diff using inspect change from README.md step 4 added moving action of existing booking. It checks bookings that are not the booking currently being moved, rejects conflicts with other active bookings, and updates the same booking object without changing the list order. I kept because moving should be moving only the target. It should reject when it has conflict with other active booking. I should update the booking object without changing the list order.

In test_student.py /test_unchanged_move_succeeds_without_self_conflict, the diff using inspect change from README.md step 4 added the test case of moving itself to the same time slot and its data should still stay the same. I kept because moving the room and time to the same room and different time, the data should stay the same. 

In test_student.py / test_same_room_overlapping_old_interval_succeeds, it tests the case that moving a same-room move whose new interval overlaps the old interval or not. I kept because moving the room and time to the same room and different time, the data should stay the same. I checked the revised diff to confirm the changing code.


remaining uncertainty yourself: At first I was not sure about the case that moving the same room same time to the same room different time, how should it reacts. But now I know that it should accept it.