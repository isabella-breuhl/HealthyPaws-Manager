



/* Delete Bella from the Database */

DELETE FROM Pet
    WHERE PetId == "1121";




/* Cancel an Appointment */

DELETE FROM Appointment
    WHERE Time == "10:00AM"
        AND Date == "2024-05-04";