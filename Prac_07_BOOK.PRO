Domains
name=string
address=string
age=integer
title=string
author=string
publisher=symbol

Predicates
author (name, address, age)
publisher (name, address)
book (title, author, publisher)

Clauses
author ("Vidhi","Surat",20).
author ("Preet","Mumbai",21).
author ("Parth","Mumbai",21).

publisher ("Honey", "Baroda").
publisher ("Liza", "Rajkot").
publisher ("Krishna", "Ahmedabad").

book ("Secrets", "Preet", "Honey").
book ("Warmth", "Vidhi", "Liza").
book ("lies", "Parth", "Krishna").

% Facts
author(john, '123 Main St', 35).
author(susan, '456 Elm St', 42).
author(david, '789 Oak St', 28).
publisher(abc, '100 Publisher Ave').
publisher(xyz, '200 Publisher Rd').
book('Book 1', john, abc).
book('Book 2', susan, abc).
book('Book 3', david, xyz).
book('Book 4', john, xyz).

% Rules to answer the questions

% a. What are the names of all authors?
all_authors(Names) :-
    findall(Name, author(Name, _, _), Names).

% b. What is the address of publisher abc?
publisher_address(PublisherName, Address) :-
    publisher(PublisherName, Address).

% c. What are the titles published by abc?
titles_published_by(PublisherName, Titles) :-
    findall(Title, (book(Title, _, PublisherName)), Titles).

% Example queries:
% a. What are the names of all authors?
% ?- all_authors(Names).
%
% b. What is the address of publisher abc?
% ?- publisher_address(abc, Address).
%
% c. What are the titles published by abc?
% ?- titles_published_by(abc, Titles).
