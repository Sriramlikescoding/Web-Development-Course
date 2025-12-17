create TABLE dinnerSpots(
Name text,
Neighborhood text,
Cuisine text,
Review real,
Price text,
Health text
);

insert into dinnerSpots VALUES
('Sriram', 'MidTown', 'Korean', 4.6, '58', 'B'),
('Bob', 'West Side', 'Pizza', 2.1, '13', 'B'),
('Heath', 'East Side', 'Burgers', 3.8, '24', ''),
('Ledger', 'East Side', 'Chinese', 4.6, '38', ''),
('Nicolas', 'MidTown', 'Steak', 5.0, '50', 'A'),
('Cage', 'Brooklyn', 'Italian', 1.2, '40', 'B'),
('Andrew', 'Brooklyn', 'Burgers', 3.5, '24', ''),
('Andy', 'East Side', 'Pizza', 4.2, '12', 'B'),
('Lucas', 'MidTown', 'Mexican', 3.8, '10', 'B'),
('Lilian', 'West Side', 'Mexican', 2.5, '32', ''),
('Ian', 'Up Town', 'Pizza', 5.0, '60', 'A');

select * from dinnerSpots;
--Select distinct neighborhood from dinner spots table
select distinct Neighborhood from dinnerSpots;

--Select distinct cuisines from dinner spots table
select distinct Cuisine from dinnerSpots;

--Select all restaurants with chinese cuisine
select * from dinnerSpots where Cuisine == 'Chinese';

--Select all restaurants with reviews >= 4
select * from dinnerSpots where Review >=4;

--Select all restaurants with Italian cuisine and with price > 35

select * from dinnerSpots where Cuisine == 'Italian' and Price > 35;

--Pick up all rows which are not null
select * from dinnerSpots where Health <> null;

--Select top 4 restaurants Order by Reviews in descending order
select * from dinnerSpots order by Review desc limit 4;

--Select all records where the name starts with L
select * from dinnerSpots where name like 'L%';

--Select all records where neighborhood is midtown or east side or west tsie
select * from dinnerSpots where Neighborhood in ('Midtown', 'East Side', 'West Side');