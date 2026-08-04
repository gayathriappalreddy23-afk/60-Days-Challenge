
CREATE TABLE STUDENT (
    studentId INT,
    name VARCHAR(15),
    dept VARCHAR(10),
    fees INT
);


INSERT INTO STUDENT(studentId, name, dept, fees) VALUES (1, 'Hema', 'CSE', 20000);
INSERT INTO STUDENT(studentId, name, dept, fees) VALUES (2, 'Indu', 'ECE', 90000);
INSERT INTO STUDENT(studentId, name, dept, fees) VALUES (3, 'Anand', 'ME', 50000);
INSERT INTO STUDENT(studentId, name, dept, fees) VALUES (4, 'Rahul', 'CSE', 20000);
INSERT INTO STUDENT(studentId, name, dept, fees) VALUES (5, 'Priya', 'ECE', 90000);
INSERT INTO STUDENT(studentId, name, dept, fees) VALUES (6, 'Kiran', 'CSE', 50000);

SELECT * FROM STUDENT;

SELECT * FROM STUDENT WHERE dept = 'ECE';

Select * from STUDENT order by fees;

select * from STUDENT order by fees desc;

select distinct dept from STUDENT;

SELECT TOP 4* from STUDENT;

SELECT * from STUDENT ORDER BY name;

SELECT * FROM STUDENT ORDER BY FEES DESC;

SELECT TOP 3* FROM STUDENT;

SELECT DISTINCT DEPT FROM STUDENT;

SELECT TOP 2 * FROM STUDENT ORDER BY FEES DESC;

SELECT DEPT,FEES FROM STUDENT ORDER BY DEPT;

SELECT NAME FROM STUDENT ORDER BY NAME;

SELECT NAME,FEES FROM STUDENT WHERE FEES>40000 ORDER BY FEES DESC;

SELECT DISTINCT DEPT FROM STUDENT WHERE FEES>40000;

--output
studentId   name            dept       fees       
----------- --------------- ---------- -----------
          1 Hema            CSE              20000
          2 Indu            ECE              90000
          3 Anand           ME               50000
          4 Rahul           CSE              20000
          5 Priya           ECE              90000
          6 Kiran           CSE              50000
studentId   name            dept       fees       
----------- --------------- ---------- -----------
          2 Indu            ECE              90000
          5 Priya           ECE              90000
studentId   name            dept       fees       
----------- --------------- ---------- -----------
          1 Hema            CSE              20000
          4 Rahul           CSE              20000
          3 Anand           ME               50000
          6 Kiran           CSE              50000
          5 Priya           ECE              90000
          2 Indu            ECE              90000
studentId   name            dept       fees       
----------- --------------- ---------- -----------
          2 Indu            ECE              90000
          5 Priya           ECE              90000
          6 Kiran           CSE              50000
          3 Anand           ME               50000
          4 Rahul           CSE              20000
          1 Hema            CSE              20000
dept      
----------
CSE       
ECE       
ME        
studentId   name            dept       fees       
----------- --------------- ---------- -----------
          1 Hema            CSE              20000
          2 Indu            ECE              90000
          3 Anand           ME               50000
          4 Rahul           CSE              20000
studentId   name            dept       fees       
----------- --------------- ---------- -----------
          3 Anand           ME               50000
          1 Hema            CSE              20000
          2 Indu            ECE              90000
          6 Kiran           CSE              50000
          5 Priya           ECE              90000
          4 Rahul           CSE              20000
studentId   name            dept       fees       
----------- --------------- ---------- -----------
          2 Indu            ECE              90000
          5 Priya           ECE              90000
          6 Kiran           CSE              50000
          3 Anand           ME               50000
          4 Rahul           CSE              20000
          1 Hema            CSE              20000
studentId   name            dept       fees       
----------- --------------- ---------- -----------
          1 Hema            CSE              20000
          2 Indu            ECE              90000
          3 Anand           ME               50000
DEPT      
----------
CSE       
ECE       
ME        
studentId   name            dept       fees       
----------- --------------- ---------- -----------
          2 Indu            ECE              90000
          5 Priya           ECE              90000
DEPT       FEES       
---------- -----------
CSE              20000
CSE              20000
CSE              50000
ECE              90000
ECE              90000
ME               50000
NAME           
---------------
Anand          
Hema           
Indu           
Kiran          
Priya          
Rahul          
NAME            FEES       
--------------- -----------
Indu                  90000
Priya                 90000
Kiran                 50000
Anand                 50000
DEPT      
----------
CSE       
ECE       
ME        
studentId   name            dept       fees       
----------- --------------- ---------- -----------
          1 Hema            CSE              20000


SELECT * FROM STUDENT WHERE studentId=1;
