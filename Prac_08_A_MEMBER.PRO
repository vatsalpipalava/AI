domains
listint = integer*
listchar = string*

predicates
list_member(integer, listint)
list_member(string, listchar)

clauses
list_member(X, [X|_]).
list_member(X, [_|TAIL]) :- list_member(X, TAIL).

% A) Check if an element is a member of a list.
member(X, [X|_]).
member(X, [_|T]) :-
    member(X, T).

% B) Find the length of an input list.
length([], 0).
length([_|T], N) :-
    length(T, M),
    N is M + 1.

% C) Concatenate two lists.
concatenate([], L, L).
concatenate([H|T1], L2, [H|T3]) :-
    concatenate(T1, L2, T3).

% D) Reverse a list.
reverse_list([], []).
reverse_list([H|T], Reversed) :-
    reverse_list(T, Rest),
    concatenate(Rest, [H], Reversed).

% E) Delete an item from a list.
delete_item(_, [], []).
delete_item(X, [X|T], T).
delete_item(X, [H|T], [H|Result]) :-
    delete_item(X, T, Result).
