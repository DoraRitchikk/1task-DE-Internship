CREATE Procedure insertRooms
(@json VARCHAR(MAX) = '')
AS
BEGIN


INSERT INTO rooms
SELECT id,name
	FROM OPENJSON(@json)
	WITH (
		id int '$.id',
		name NVARCHAR(50) '$.name'
		)
END