/* All Upcoming Appointments Group 1 */

SELECT Pet.Name, Appointment.Time, Appointment.Date 
    FROM Pet JOIN Appointment
        WHERE Appointment.PetId == Pet.PetId
            AND Date BETWEEN DATE('now') AND DATE('now', '+14 days') 
            ORDER BY Date ASC, Time ASC;




 