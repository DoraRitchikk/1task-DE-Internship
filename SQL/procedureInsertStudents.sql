--Заполняем таблицу student строками из json файла

CREATE Procedure insertStudents
(@json VARCHAR(MAX) = '')
AS
BEGIN


INSERT INTO students
SELECT birthday,id,name,room,sex
	FROM OPENJSON(@json)
	WITH (
		birthday datetime2		'$.birthday',
		id	     int			'$.id',
		name	 NVARCHAR(300)  '$.name',
		room	 int			'$.room',
		sex 	 char			'$.sex'
		)
END