CREATE database task1;


USE task1
CREATE table rooms
(
	id int primary key,
	name nvarchar(300) not null
);


USE task1
CREATE table students
(
	birthday datetime2,
	id int primary key,
	name nvarchar(200) not null,
	room int not null,
	sex char(1) not null,
	CONSTRAINT CHK_Sex CHECK ((sex = 'M') OR (sex = 'F'))
);
CREATE index #ROOMIn on rooms(name)