CREATE Procedure task2ProcJSON
AS
BEGIN

SELECT top(5) rooms.id,avg(DATEDIFF(hour,students.birthday,GETDATE())/8766) as age
FROM rooms INNER JOIN students ON rooms.id = students.room
GROUP BY rooms.id
ORDER BY age asc
FOR JSON AUTO
END

--��� ��� ����� ���������� �� ������ ���� ������� ������� - ����� ������� ��������� �������� � ��������

CREATE Procedure task2ProcXML
AS
BEGIN

SELECT top(5) rooms.id,avg(DATEDIFF(hour,students.birthday,GETDATE())/8766) as age
FROM rooms INNER JOIN students ON rooms.id = students.room
GROUP BY rooms.id
ORDER BY age asc
FOR XML AUTO
END
