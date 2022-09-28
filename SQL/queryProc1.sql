CREATE Procedure task1ProcJSON
AS
BEGIN

SELECT rooms.name,COUNT(students.name) FROM rooms 
Inner Join students ON rooms.id = students.room
Group by rooms.name
for JSON AUTO
END

--Так как перед процедурой не должны идти никакие символы - чтобы создать процедуру выделяем её курсором

CREATE Procedure task1ProcXML
AS
BEGIN

SELECT rooms.name,COUNT(students.name) FROM rooms 
Inner Join students ON rooms.id = students.room
Group by rooms.name
for XML AUTO
END

