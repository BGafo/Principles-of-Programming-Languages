Problem 1
Write a function

count123 : int list -> int * int * int
that takes in an int list l and returns a 3-tuple of integers counting the number of 1's, 2's and 3's respectively in l. For example, count123 [3;4;2;1;3] = (1,1,2), and count123 [4;4;1;2;1] = (2,1,0).

let count123 l =
  (* YOUR CODE HERE *)
assert (count123 [3;4;2;1;3] = (1,1,2))


Problem 2
Write a function

n_times : ('a -> 'a) * int * 'a -> 'a
such that n_times (f,n,v) applies f to v n times. For example, n_times((fun x-> x+1), 50, 0) = 50. If n<=0 return v.

let rec n_times (f, n, v) =
  (* YOUR CODE HERE *)
assert (n_times ((fun x-> x+1), 50, 0) = 50)


Problem 3 
Write a function

buckets : ('a -> 'a -> bool) -> 'a list -> 'a list list
that partitions a list into equivalence classes. That is, buckets equiv lst should return a list of lists where each sublist in the result contains equivalent elements, where two elements are considered equivalent if equiv returns true. For example:

buckets (=) [1;2;3;4] = [[1];[2];[3];[4]]
buckets (=) [1;2;3;4;2;3;4;3;4] = [[1];[2;2];[3;3;3];[4;4;4]]
buckets (fun x y -> (=) (x mod 3) (y mod 3)) [1;2;3;4;5;6] = [[1;4];[2;5];[3;6]]
The order of the buckets must reflect the order in which the elements appear in the original list. For example, the output of buckets (=) [1;2;3;4] should be [[1];[2];[3];[4]] and not [[2];[1];[3];[4]] or any other permutation.

The order of the elements in each bucket must reflect the order in which the elements appear in the original list. For example, the output of buckets (fun x y -> (=) (x mod 3) (y mod 3)) [1;2;3;4;5;6] should be [[1;4];[2;5];[3;6]] and not [[4;1];[5;2];[3;6]] or any other permutations.

Assume that the comparison function ('a -> 'a -> bool) is commutative, associative and idempotent.

Just use lists. Do not use sets or hash tables.

List append function @ may come in handy. [1;2;3] @ [4;5;6] = [1;2;3;4;5;6].

let buckets p l =
  (* YOUR CODE HERE *)
assert (buckets (=) [1;2;3;4] = [[1];[2];[3];[4]]);
assert (buckets (=) [1;2;3;4;2;3;4;3;4] = [[1];[2;2];[3;3;3];[4;4;4]]);
assert (buckets (fun x y -> (=) (x mod 3) (y mod 3)) [1;2;3;4;5;6] = [[1;4];[2;5];[3;6]])
Tail Recursion


Problem 4
The usual recursive formulation of fibonacci function

let rec fib n = 
  if n = 0 then 0
  else if n = 1 then 1
  else fib (n-1) + fib (n-2)
has exponential running time. It will take a long time to compute fib 50. You might have to interrupt its execution if you did try to do fib 50 in the notebook.

But we know that fibonacci number can be computed in linear time by remembering just the current cur and the previous prev fibonacci number. In this case, the next fibonacci number is computed as the sum of the current and the previous numbers. Then the program continues by setting prev to be cur and cur to be cur + prev.

Implement a tail recursive function fib_tailrec that uses this idea and computes the nth fibonacci number in linear time.

fib_tailrec : int -> int
let fib_tailrec n =
  (* YOUR CODE HERE *)
assert (fib_tailrec 50 = 12586269025)
Map and Fold
For the following problems, you must only use List.map, List.fold_left, or List.fold_right to complete these functions, so no functions should be defined using the rec keyword. You will lose points if this rule is not followed.

Some of these functions will require just List.map or List.fold_left, but some will require a combination of the two. The map/reduce design pattern may come in handy, e.g. map over a list to convert it to a new list which you then process a second time using fold. The idea is that you first process the list using map, and then reduce the resulting list using fold.


Problem 5
Write a function

assoc_list: 'a list -> ('a * int) list
that, given a list, returns a list of pairs where the first value of each pair represents an element of the list and the second integer of the pair represents the number of occurrences of that element in the list. This associative list should not contain duplicates. Order does not matter. For example, assoc_list [1; 2; 2; 1; 3] = [(2,2); (1, 2); (3, 1)].

let assoc_list l =
  (* YOUR CODE HERE *)
assert (assoc_list [1; 2; 2; 1; 3] = [(2,2); (1, 2); (3, 1)])


Problem 6
Write a function

ap: ('a -> 'b) list -> 'a list -> 'b list
ap fs args applies each function in fs to each argument in args in order. For example, ap [(fun x -> x^"?"); (fun x -> x^"!")] ["foo";"bar"] = ["foo?";"bar?";"foo!";"bar!"] where ^ is an OCaml operator for string concatenation.

let ap fs args = 
  (* YOUR CODE HERE *)
assert (ap [(fun x -> x^"?"); (fun x -> x^"!")] ["foo";"bar"] = ["foo?";"bar?";"foo!";"bar!"])


Problem 7
Write a function

maxl2: int list -> int
maxl2 lst takes as input a list lst of positive integers and returns the maximum sum of any two elements of the list. For example, maxl2 [1;10;2;100;3;400] = 500. If lst contains less than 2 elements, return 0.

let maxl2 lst = 
  (* YOUR CODE HERE *)
assert (maxl2 [1;10;2;100;3;400] = 500)
assert (maxl2 [100;30;2;100;3;100] = 200)
Datatypes:
Problems 8-9 are about manipulating tree data structures.

In OCaml, you can define a tree data structure using datatype:

type 'a tree = Leaf | Node of 'a tree * 'a * 'a tree
We will assume binary search trees in this assignment and can define a bineary search tree insertion function as the following:

let rec insert tree x =
  match tree with
  | Leaf -> Node(Leaf, x, Leaf)
  | Node(l, y, r) ->
     if x = y then tree
     else if x < y then Node(insert l x, y, r)
     else Node(l, y, insert r x)
We can construct a binary search tree from a list:

let construct l =
  List.fold_left (fun acc x -> insert acc x) Leaf l


Problem 8
We have seen the benefits of the 'fold' function for list data structures. In a similar fashion, write a function

fold_inorder : ('a -> 'b -> 'a) -> 'a -> 'b tree -> 'a
That does an inorder fold of the tree. The function should traverse the left subtree, visit the root, and then traverse the right subtree. For example,

fold_inorder (fun acc x -> acc @ [x]) [] (Node (Node (Leaf,1,Leaf), 2, Node (Leaf,3,Leaf))) = [1;2;3]

let rec fold_inorder f acc t =
  (* YOUR CODE HERE *)
assert (fold_inorder (fun acc x -> acc @ [x]) [] (Node (Node (Leaf,1,Leaf), 2, Node (Leaf,3,Leaf))) = [1;2;3]);
assert (fold_inorder (fun acc x -> acc + x) 0 (Node (Node (Leaf,1,Leaf), 2, Node (Leaf,3,Leaf))) = 6)


Problem 9
Given a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

levelOrder : 'a tree -> 'a list list
Example: Given a tree t:

the returned result of levelOrder t should be a nested list [[41];[20;65];[11;29;50;91];[32;72;99]]. The ith elment of the nested list is a list of tree elements at the ith level of the tree t from left to right. You may need to define a recursive auxiliary function.

Note: OCaml queues are mutable first-in-first-out (FIFO) data structures, and hence are not functional. Since our goal is to practice functional programming, please do not use OCaml queues for this assignment.

You may find the List.mapi function particularly useful.

let levelOrder t =
    (* YOUR CODE HERE *)
assert (levelOrder (construct [41;65;20;11;50;91;29;99;32;72]) = [[41];[20;65];[11;29;50;91];[32;72;99]])
