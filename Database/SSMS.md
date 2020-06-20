# What is Dayabase:
A database is a data structure that stores organized information. Most databases contain multiple tables, which may each include several different fields. ... These sites use a database management system (or DBMS)


--------------------------------------------------------------------------------------------

Types of Database Management Systems

- Hierarchical databases.
- Network databases.
- Relational databases.
- Object-oriented databases.
- Graph databases.
- ER model databases.
- Document databases.
- NoSQL databases.

----------------------------------------------------------------------



CREATE DATABASE Student

USE Student

---------------------------------------------------------------------------------------------------------------------------------------------

CREATE TABLE Student_Information
(

ID INT PRIMARY KEY IDENTITY (1,1),
FIRST_Name CHAR (100) NOT NULL,
LAST_Name CHAR (100) NOT NULL,
CITY VARCHAR (50),
AGE INT ,

);

INSERT INTO Student_Information ([FIRST_Name],[LAST_Name],[CITY],[AGE])
VALUES ('Saumya','BHATT','VALSAD',21);

INSERT INTO Student_Information ([FIRST_Name],[LAST_Name],[CITY],[AGE])
VALUES ('Deepak','BHAVSAR','SURAT',23);

INSERT INTO Student_Information ([FIRST_Name],[LAST_Name],[CITY],[AGE])
VALUES ('Foram','PATEL','VALSAD',20);

INSERT INTO Student_Information ([FIRST_Name],[LAST_Name],[CITY],[AGE])
VALUES ('Vini','PATEL','VALSAD',20);

INSERT INTO Student_Information ([FIRST_Name],[LAST_Name],[CITY],[AGE])
VALUES ('Mili','JAVIA','VALSAD',22);

drop table Student_Information;
---------------------------------------------------------------------------------------------------------------------------------------

SELECT * FROM Student_Information;

SELECT TOP(3) * FROM Student_Information;

SELECT FIRST_Name,* FROM Student_Information;

SELECT FIRST_Name FROM Student_Information;

select FIRST_Name
from Student_Information
where FIRST_Name like 'Sa%'

---------------------------------------------------------------------------------------------------------------------------------------

UPDATE Student_Information SET CITY = 'VALSAD' WHERE FIRST_Name = 'Saumya';

----------------------------------------------------------------------------------------------------------------------------------------

DELETE Student_Information WHERE FIRST_Name='Deepak';

----------------------------------------------------------------------------------------------------------------------------------------

ALTER TABLE Student_Information ADD COUNTRY VARCHAR (50);

----------------------------------------------------------------------------------------------------------------------------------------

UPDATE Student_Information SET COUNTRY = 'INDIA';

UPDATE Student_Information SET COUNTRY = 'USA' where FIRST_Name='Mili';


------------------------------------------------------------------------------------------------------------------------------------------

CREATE TABLE Course
(

ID INT PRIMARY KEY IDENTITY (1,1),
Course_Name VARCHAR (100) ,
No_of_Students int ,

);

SELECT * FROM Course;


INSERT INTO Course ([Course_Name],[No_of_Students] )
VALUES ('Physics',20);

INSERT INTO Course ([Course_Name],[No_of_Students] )
VALUES ('Biology',35);

INSERT INTO Course ([Course_Name],[No_of_Students] )
VALUES ('Social Science',40);

INSERT INTO Course ([Course_Name],[No_of_Students] )
VALUES ('Computer',100);

INSERT INTO Course ([Course_Name],[No_of_Students] )
VALUES ('Chemistry',10);

drop table Course
------------------------------------------------------------------------------------------------------------------------------------------


CREATE TABLE Class_Number
(

ORDER_ID INT PRIMARY KEY IDENTITY (1,1),
Class char (2),
Course_ID INT FOREIGN KEY REFERENCES Course(ID) ,
Student_Information_ID INT FOREIGN KEY REFERENCES Student_Information(ID),

);


SELECT * FROM Class_Number;

INSERT INTO Class_Number ([Class],[Course_ID],[Student_Information_ID])
VALUES ('A',1,1)

INSERT INTO Class_Number ([Class],[Course_ID],[Student_Information_ID])
VALUES ('B',1,2)

INSERT INTO Class_Number ([Class],[Course_ID],[Student_Information_ID])
VALUES ('C',1,4)

INSERT INTO Class_Number ([Class],[Course_ID],[Student_Information_ID])
VALUES ('B',1,3)

INSERT INTO Class_Number ([Class],[Course_ID],[Student_Information_ID])
VALUES ('A',2,4)

INSERT INTO Class_Number ([Class],[Course_ID],[Student_Information_ID])
VALUES ('A',4,4)

INSERT INTO Class_Number ([Class],[Course_ID],[Student_Information_ID])
VALUES ('C',3,4)

INSERT INTO Class_Number ([Class],[Course_ID],[Student_Information_ID])
VALUES ('B',5,5)

drop table Class_Number;

------------------------------------------------------------------------------------------------------------------------------------------------------


SELECT * FROM Class_Number AS O 
INNER JOIN Course P ON
O.Course_ID = P.ID
INNER JOIN Student_Information C ON
O.Student_Information_ID = C.ID;


SELECT C.ID,C.FIRST_Name,P.Course_Name,P.No_of_Students,O.Class FROM Class_Number AS O 
INNER JOIN Course P ON
O.Course_ID = P.ID
INNER JOIN Student_Information C ON
O.Student_Information_ID = C.ID;

--------------------------------------------------------------------------------------------------------------------------------------------------------