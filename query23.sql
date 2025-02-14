/* Get all the upcoming pet birthdays this month from current patients of this lcoation (more than just once) */
/* Group 2 */

SELECT Pet.Name, Pet.Birthday
    FROM Pet JOIN Record
        WHERE Record.PetId == Pet.PetId
            AND Pet.Birthday BETWEEN DATE('now') AND DATE('now', '+30 days') 
            AND Record.Location == "3103 Aurora Road, Joy Washington"
            GROUP BY Pet.Name 
            HAVING COUNT(*) > 1 
            ORDER BY Birthday ASC;

            