/* YOUR CODE HERE (Problem 1, delete the following line) */
append([], Q, Q).
append([H | P], Q ,[H | R]):- append(P, Q, R).
reverseL([],[]).
reverseL([H | T], N):- reverseL(T, N1), append(N1, [H], N).

?- reverseL([],X).
?- reverseL([1,2,3],X).
?- reverseL([a,b,c],X).


/* YOUR CODE HERE (Problem 2, delete the following line) */
remov(X, [], []).    
remov(H, [H| T], List):- remov(H, T, List).
remov(H, [Hnext | T], List):- remov(H, T, List1), List = [Hnext | List1].
remove_duplicates([], []).
remove_duplicates([H | T], List):- remov(H, T, Acc), remove_duplicates(Acc, Acc1), List = [H | Acc1].

?- remove_duplicates([1,2,3,4,2,3],X).
?- remove_duplicates([1,4,5,4,2,7,5,1,3],X).
?- remove_duplicates([], X).


/* Your CODE HERE (Problem 3, delete the following line) */
assoc([], P, [P-1]).
assoc([P1-P2|T], P1, [P1-P2prime|T]) :- P2prime is P2 + 1.
assoc([P1-P2|T1], P, [P1-P2|T2]) :- P1 \= P, assoc(T, P, T2).

assoc_list([], []).
assoc_list([H|T], Res) :- assoc_list([], Tprime), assoc(Tprime, H, Res); 
keysort(Res, X).

?- assoc_list([1], [1-1]).
?- assoc_list([1,1,2,2,2,3,1], [1-3, 2-3, 3-1]).
?- assoc_list([1,1,4,2,2,2,3,1,1,3,1], X).


/* YOUR CODE HERE (Problem 4, delete the following line) */
intersectionL([], _, []).
intersectionL([H|T], L2, [H|T2]):- member(H, L2), intersectionL(T, L2, T2).
intersectionL([_|T], L2, L3):- intersectionL(T, L2, L3).

?- intersectionL([1,2,3,4],[1,3,5,6],[1,3]).
?- intersectionL([1,2,3,4],[1,3,5,6],X).
?- intersectionL([1,2,3],[4,3],[3]).


/* YOUR CODE HERE (Problem 5, delete the following line) */
len([], 0).
len([H|T], N):- len(T, M), N is M+1.

quicksort([H|T],SL) :-
  partition(T,H,Ls,Rs), quicksort(Ls,SLs), quicksort(Rs,SRs), append(SLs,[H|SRs],SL).
quicksort([],[]).

partition([],Y,[],[]).
partition([X|Xs],Y,[X|Ls],Rs) :- X =< Y, partition(Xs,Y,Ls,Rs).
partition([X|Xs],Y,Ls,[X|Rs]) :- X > Y, partition(Xs,Y,Ls,Rs).
partition([H|T], R):- partition([H|T], H, [], []).

maxL3([H|T], Sum):- len([H|T], Sum1), Sum2 = Sum1, Sum2 > 2, quicksort([H|T], Res), find_max3(Res, Final), Sum = Final.


find_max3([X,Y,Z], N):- 
N is X + Y + Z.
find_max3([H|T], N):- find_max3(T, N).

?- not(maxL3([1], X)).
?- maxL3([1,2,3,4], 9).
?- maxL3([10,3,2,3,10], X).
/* YOUR CODE HERE (Problem 6, delete the following line) */
prefix(P,L) :- append(P,_,L).
suffix(S,L) :- append(_,S,L).

partition([],[],[]).
partition([X],[X],[]).
partition(L, P, S):- append(P, S, L), len(P, N), len(S, N).
partition(L, P, S):- append(P, S, L), len(P, N), N1 is N+1, len(S, N1).
partition(L, P, S):- append(P, S, L), len(P, N), N1 is N-1, len(S, N1).

?- partition([a],[a],[]).
?- partition([1,2,3],[1],[2,3]).
?- partition([a,b,c,d],X,Y).


/* YOUR CODE HERE (Problem 7, delete the following line) */
merge([], [], []).
merge([X], [], [X]).
merge([], [X], [X]).
merge([H1|T1], [H2|T2], [H1|List]):- H1 =< H2, merge(T1, [H2|T2], List).
merge([H1|T1], [H|T2], [H|List]):- merge([H1|T1], T2, List).

?- merge([],[1],[1]).
?- merge([1],[],[1]).
?- merge([1,3,5],[2,4,6],X).


/* YOUR CODE HERE (Problem 8, delete the following line) */
mergesort([],[]).
mergesort([X],[X]).
mergesort(L,SL):- partition(L, LL, RL), mergesort(LL, SL1), mergesort(RL, SL2), merge(SL1, SL2, SL).

?- mergesort([3,2,1],X).
?- mergesort([1,2,3],Y).
?- mergesort([],Z).
