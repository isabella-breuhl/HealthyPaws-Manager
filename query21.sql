/* Owners with One Pet Group 3 */

SELECT Owner.FirstName, Owner.LastName, Owner.Phone
  FROM Owner
    WHERE Owner.OwnerId IN ( SELECT Owner.OwnerId
                              FROM Pet
                                GROUP BY Owner.OwnerId
                                HAVING COUNT(*) == 1)
        ORDER BY Owner.LastName ASC;

 
 