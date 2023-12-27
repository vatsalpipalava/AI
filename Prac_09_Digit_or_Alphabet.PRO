predicates
check(char)
go

clauses
go:-
write("Enter the character:"), readchar (N), write(N), nl, check(N).
check(N):-N>=47,N<=57, write(N," is a digit.").
check (N) :- N>=65,N<=90, write(N," is a uppercase letter.").
check(N) :- N>=97,N<=122, write(N," is a lowercase letter."), write(N," is a symbol."), nl.
