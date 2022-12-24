Problem 1
Write a function

range : int -> int -> int list
such that range num1 num2 returns an ordered list of all integers from num1 to num2 inclusive. For example, range 2 5 = [2;3;4;5]. Return [] if num2 < num1.

let rec range num1 num2 =
  (* YOUR CODE HERE *)
assert (range 2 5 = [2;3;4;5])
Problem 2
Write a function

flatten : 'a list list -> 'a list
that flattens a list. For example, flatten [[1;2];[4;3]] = [1;2;4;3].

let rec flatten l =
  (* YOUR CODE HERE *)
assert (flatten ([[1;2];[4;3]]) = [1;2;4;3])
Problem 3
Write a function

remove_stutter : 'a list -> 'a list
that removes stuttering from the original list. For example, remove_stutter [1;2;2;3;1;1;1;4;4;2;2]= [1;2;3;1;4;2].

let remove_stutter l =
  (* YOUR CODE HERE *)
assert (remove_stutter [1;2;2;3;1;1;1;4;4;2;2] = [1; 2; 3; 1; 4; 2])
Problem 4 (3 questions)
Set Implementation using Lists

For this part of the project, you will implement sets. In practice, sets are implemented using data structures like balanced binary trees or hash tables. However, your implementation must represent sets using lists. While lists don’t lend themselves to the most efficient possible implementation, they are much easier to work with.

For this project, we assume that sets are unordered, homogeneous collections of objects without duplicates. The homogeneity condition ensures that sets can be represented by OCaml lists, which are homogeneous. The only further assumptions we make about your implementation are that the empty list represents the empty set, and that it obeys the standard laws of set theory. For example, if we insert an element x into a set a, then ask whether x is an element of a, your implementation should answer affirmatively.

Finally, note the difference between a collection and its implementation. Although sets are unordered and contain no duplicates, your implementation using lists will obviously store elements in a certain order and may even contain duplicates. However, there should be no observable difference between an implementation that maintains uniqueness of elements and one that does not; or an implementation that maintains elements in sorted order and one that does not.

Our testcases do not use input lists with duplicated elements.

If you do not feel comfortable with sets, see the Set Wikipedia Page and/or this Set Operations Calculator.

We provide some example code.

elem : 'a -> 'a list -> bool
elem x a returns true iff x is an element of the set a. For example, elem 5 [2;3;5;7;9] = true.

let rec elem x a =
  match a with
  | [] -> false
  | h::t -> if h = x then true else elem x t
subset: 'a list -> 'a list -> bool
subset a b returns true iff a is a subset of b. For example, subset [5] [2;3;5;7;9] = true.

let rec subset a b =
  match a with
  | [] -> true
  | h::t -> if elem h b then subset t b else false
eq: 'a list -> 'a list -> bool
eq a b returns true iff a and b are equal as sets. For example, eq [5;3;2;9;7] [2;3;5;7;9] = true.

let rec eq a b =
  (subset a b) && (subset b a)
You need to implement the following three functions:

remove: 'a -> 'a list -> 'a list
remove x a removes x from the set a. For example, eq (remove 5 [2;3;5;7;9]) [2;3;9;7] = true.

let rec remove x a =
  (* YOUR CODE HERE *)
assert (eq (remove 5 []) []);
assert (eq (remove 5 [2;3;5;7;9]) [2;3;9;7]);
assert (eq (remove 4 [2;3;5;7;9]) [2;3;5;9;7]);
union: 'a list -> 'a list -> 'a list
union a b returns the union of the sets a and b. For example, eq (union [5;2] [3;7;9]) [2;3;5;7;9] = true.

let rec union a b =
  (* YOUR CODE HERE *)
assert (eq (union [2;3;5] []) [2;3;5]);
assert (eq (union [5;2] [3;7;9]) [2;3;5;9;7]);
assert (eq (union [2;3;9] [2;7;9]) [2;3;9;7]);
diff: 'a list -> 'a list -> 'a list
diff a b returns the difference of sets a and b in a, i.e. diff a b contains the elements of a that are not in b. For example, eq (diff [1;3;2] [2;3]) [1] = true.

let rec diff a b =
  (* YOUR CODE HERE *)
assert (eq (diff [1;3;2] [2;3]) [1]);
assert (eq (diff ['a';'b';'c';'d'] ['a';'e';'i';'o';'u']) ['b';'c';'d']);
assert (eq (diff ["hello";"ocaml"] ["hi";"python"]) ["hello";"ocaml"]);
Problem 5 (3 questions)
Write an OCaml function

digitsOfInt : int -> int list
such that digitsOfInt n returns [] if n is less than zero, and returns the list of digits of n in the order in which they appear in n. You may use the mod operator, e.g. 321 mod 23 = 22.

let rec digitsOfInt n = 
  (* YOUR CODE HERE *)
assert (digitsOfInt 3124 = [3;1;2;4]);
assert (digitsOfInt 352663 = [3;5;2;6;6;3]);
Consider the process of taking a number, adding its digits, then adding the digits of the number derived from it, etc., until the remaining number has only one digit. The number of additions required to obtain a single digit from a number n is called the additive persistence of n, and the digit obtained is called the digital root of n. For example, the sequence obtained from the starting number 9876 is 9876, 30, 3, so 9876 has an additive persistence of 2 and a digital root of 3.

Write two OCaml functions:

additivePersistence : int -> int
digitalRoot : int -> int
that take positive integer arguments n and return respectively the additive persistence and the digital root of n.

let additivePersistence n =
  (* YOUR CODE HERE *)

let digitalRoot n =
  (* YOUR CODE HERE *)
assert (additivePersistence 9876 = 2);
assert (digitalRoot 9876 = 3);
