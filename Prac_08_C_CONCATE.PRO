domains
l1=integer*

predicates
list_concate(l1,l1,l1)

clauses
list_concate([],L,L).
list_concate([H|T],L2,[H|L3]) :- list_concate(T,L2,L3).