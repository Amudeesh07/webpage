create database edb;
use edb;
create table user(
ID integer auto_increment primary key,
NAME varchar(50),
REGNO integer,
RANKK integer,
MAIL varchar(50),
PASSWORD varchar(50),
q1 integer,
q2 integer,
q3 integer,
q4 integer,
q5 integer
);
select * from user;
alter table user add SCORE integer; 
update user set rankk=1 where id=14;
insert into user(name,regno,rankk,q1,q2,q3,q4,q5,SCORE) values ('Sinduja',20229,10,9,9,9,9,8,45);
