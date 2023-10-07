domains
    intlist = integer*
    charlist = string*
predicates
    list_length(integer, intlist)
    list_length(integer, charlist)
clauses
    list_length(0, []).
    list_length(N, [_|T]):-
        list_length(N1, T),
        N is 1 + N1.
