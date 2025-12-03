-- Create A Student Table Wtih Columns ID, Name, Score-Eng, Score-Lit, Score-Math, Score-Sci

CREATE TABLE student(
    ID integer PRIMARY KEY,
     Name text,
     Country text,
    Score_Eng integer,
     Score_Lit integer,
    Score_Math integer,
    Score_Sci integer);

insert into student(ID, Name, Country, Score_Eng, Score_Lit, Score_Math, Score_Sci)
VALUES 
(1, 'Sriram', 'U.S.A.', 84, 92, 89, 98),
(2, 'Lucy', 'U.S.A.', 98, 82, 40, 100),
(3, 'Cyrus', 'Germany', 99, 67, 87, 79),
(4, 'Lucas', 'Germany', 67, 81, 89, 85),
(5, 'Guy', 'Germany', 100, 76, 70, 79),
(6, 'Brian', 'France', 69, 79, 100, 92);

select * from student;
select distinct Country from student;
select count( distinct Country) from student;
select count( Country) from student;
select count( ID) from student where Score_Lit > 70;
select sum(Score_Lit) from student;
select avg(Score_Lit) from student;