USE task1


CREATE Procedure task4ProcJSON
AS
BEGIN

SELECT distinct rooms.id FROM rooms inner join students
on rooms.id = students.room
where students.sex IN ('F','M')
ORDER BY rooms.id
for JSON AUTO
END

CREATE Procedure task4ProcXML
AS
BEGIN

SELECT distinct rooms.id FROM rooms inner join students
on rooms.id = students.room
where students.sex IN ('F','M')
ORDER BY rooms.id
for XML AUTO
END