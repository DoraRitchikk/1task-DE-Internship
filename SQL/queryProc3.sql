CREATE Procedure task3ProcJSON
AS
BEGIN

SELECT a.room, max(DATEDIFF(YEAR,a.birthday,b.birthday))
FROM students a, students b
GROUP BY a.room,b.room,a.birthday,b.birthday
FOR JSON AUTO 
END

--Так как перед процедурой не должны идти никакие символы - чтобы создать процедуру выделяем её курсором

CREATE Procedure task3ProcXML
AS
BEGIN

SELECT a.room, max(DATEDIFF(YEAR,a.birthday,b.birthday))
FROM students a, students b
GROUP BY a.room,b.room,a.birthday,b.birthday
FOR XML AUTO 
END
