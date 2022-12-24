Problem 1
Implement reverse of a list using the predicate reverseL(X,RevX) where RevX is the reverse of the list X. You might want to use append.

/* YOUR CODE HERE (delete the following line) */
reverseL(X,RevX) :- false.
Added 1 clause(s).
Test-cases
?- reverseL([],X).
/* expected output: X = [  ]. */

?- reverseL([1,2,3],X).
/* expected output: X = [ 3, 2, 1 ]. */

?- reverseL([a,b,c],X).
/* expected output: X = [ c, b, a ]. */
X = [  ] .
X = [ 3, 2, 1 ] .
X = [ c, b, a ] .


Problem 2
Write a Prolog predicate remove_duplicates(L1,L2) that is true if L2 is equal to the result of removing all duplicate elements from L1. L1 is fully-instantiated (i.e. contains no variables). In the result, the order of the elements must be the same as the order in which the (first occurrences of the) elements appear in L1.

/* YOUR CODE HERE (delete the following line) */
remove_duplicates(L1,L2) :- false.
Added 1 clause(s).
Test-cases:
?- remove_duplicates([1,2,3,4,2,3],X).
/* expected output: X = [1, 2, 3, 4] . */

?- remove_duplicates([1,4,5,4,2,7,5,1,3],X).
/* expected output: X = [1, 4, 5, 2, 7, 3] . */

?- remove_duplicates([], X).
/* expected output: X = [] . */
X = [ 1, 2, 3, 4 ] .
X = [ 1, 4, 5, 2, 7, 3 ] .
X = [  ] .


Problem 3
Write a Prolog predicate assoc_list(L,AL) that takes in a fully-instantiated (i.e. contains no variables) list L and is true if AL is equal to the association list of L. An association list is a list consisting of pairs E-C of an element E of L and C, its number of occurrences in L. The associative list should not contain any duplicates. In Prolog, we use A-B for a pair of elements A and B. For example, 1-2 is a pair (1,2). In the result, the order of the elements must be the same as the order in which the (first occurrences of the) elements appear in L. You may need to write helper predicates.

/* Your CODE HERE (delete the following line) */
assoc_list(L,AL) :- false.
Added 1 clause(s).
Test-cases:
?- assoc_list([1], [1-1]).
/* expected output: true . */

?- assoc_list([1,1,2,2,2,3,1], [1-3,2-3,3-1]).
/* expected output: true . */

?- assoc_list([1,1,4,2,2,2,3,1,1,3,1], X).
/* expected output: X = [1-5,4-1,2-3,3-2] . */
true .
true .
X = [ 1-5, 4-1, 2-3, 3-2 ] .


Problem 4
Write a Prolog predicate intersectionL(L1,L2,L3) that is true if L3 is equal to the list containing intersection of the elements in L1 and L2 without any duplicates. In other words, L3 should contain the elements that both in L1 and in L2. The order of the elements in L3 should be the same as the order in which the elements appear in L1.

/* YOUR CODE HERE (delete the following line) */
intersectionL(L1,L2,L3) :- false.
Added 1 clause(s).
Test-cases:
?- intersectionL([1,2,3,4],[1,3,5,6],[1,3]).
/* expected output: true. */

?- intersectionL([1,2,3,4],[1,3,5,6],X).
/* expected output: X = [1,3]. */

?- intersectionL([1,2,3],[4,3],[3]).
/* expected output: true. */
true.
X = [ 1, 3 ] .
true.


Problem 5
Write a Prolog predicate maxL3(L,X) that takes in a fully-instantiated (i.e. contains no variables) integer list L and is true if X is equal to the maximum sum of any three elements in L. If L contains less than three elements, maxL3 should be false. You may need to write helper predicates.

/* Your CODE HERE (delete the following line) */
maxL3(L,X) :- false.
Added 1 clause(s).
Test-cases:
?- not(maxL3([1], X)).
/* expected output: true . */

?- maxL3([1,2,3,4], 9).
/* expected output: true . */

?- maxL3([10,3,2,3,10], X).
/* expected output: X = 23 . */
true .
true .
X = 23 .


Problem 6
Implement partition(L,P,S) such that

P is the prefix of L and
S is the suffix of L and
append(P,S,L) holds
If L is [], then P and S are [].
If L is [H], then P is [H] and S is [].
Otherwise,
let length of L be N. Then length of P is div(N/2). Use Prolog's built-in integer division.
length of S is N - div(N/2).
You may need to use the length,prefix,suffix,append predicates that we have seen in class.

prefix(P,L) :- append(P,X,L).                                                       
suffix(S,L) :- append(X,S,L).                                                       

/* YOUR CODE HERE (delete the following line) */
partition(L,P,S) :- false.
Added 3 clause(s).
Test-cases
?- partition([a],[a],[]).
/* expected output: true. */

?- partition([1,2,3],[1],[2,3]).
/* expected output: true. */

?- partition([a,b,c,d],X,Y).
/* expected output: Y = [ c, d ], X = [ a, b ]. */
true.
true.
Y = [ c, d ], X = [ a, b ] .


Problem 7
Implement the predicate merge(X,Y,Z) where X and Y are sorted, and Z contains the same elements as U where append(X,Y,U) but Z is also additionally sorted.

/* YOUR CODE HERE (delete the following line) */
merge(X,Y,Z) :- false.
Added 1 clause(s).
Test-cases
?- merge([],[1],[1]).
/* expected output: true. */

?- merge([1],[],[1]).
/* expected output: true. */

?- merge([1,3,5],[2,4,6],X).
/* expected output: X = [ 1, 2, 3, 4, 5, 6 ]. */
true.
true.
X = [ 1, 2, 3, 4, 5, 6 ] .
Problem 8
Implement predicate mergesort(L,SL) where SL is the sorted version of L, and L is fully-instantiated. Use the predicate partition to partition the list L into two segments, sort each on separately (using mergesort) and combine the individual sorted list using merge.

/* YOUR CODE HERE (delete the following line) */
mergesort(L,SL) :- false.
Added 1 clause(s).
Test-cases
?- mergesort([3,2,1],X).
/* expected output: X = [ 1, 2, 3 ]. */

?- mergesort([1,2,3],Y).
/* expected output: Y = [ 1, 2, 3 ]. */

?- mergesort([],Z).
/* expected output: Z = [  ]. */

?- mergesort([1,3,5,2,4,6],X).
/* expected output: X = [ 1, 2, 3, 4, 5, 6 ]. */
X = [ 1, 2, 3 ] .
Y = [ 1, 2, 3 ] .
Z = [  ] .
X = [ 1, 2, 3, 4, 5, 6 ] .
