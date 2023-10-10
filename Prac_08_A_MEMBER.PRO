domains
listint = integer*
listchar = string*

predicates
list_member(integer, listint)
list_member(string, listchar)

clauses
list_member(X, [X|_]).
list_member(X, [_|TAIL]) :- list_member(X, TAIL).
