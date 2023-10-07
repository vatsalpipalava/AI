domains
    cell = c(integer, integer)
    list = cell*
    int_list = integer*
predicates
    solution(list)
    member(integer, int_list)
    nonattack(cell, list)
clauses
    solution([]).
    
    solution([c(X, Y) | Others]) :-
        solution(Others),
        member(Y, [1, 2, 3, 4, 5, 6, 7, 8]),
        nonattack(c(X, Y), Others).
    
    nonattack(_, []).
    
    nonattack(c(X, Y), [c(X1, Y1) | Others]) :-
        Y <> Y1,
        Y1 - Y <> X1 - X,
        Y1 - Y <> X - X1,
        nonattack(c(X, Y), Others).
    
    member(X, [X | _]).
    
    member(X, [_ | Z]) :-
        member(X, Z).