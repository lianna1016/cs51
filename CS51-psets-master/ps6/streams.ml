(*********************************** trees ************************************)
(* Here we provide a definition for infinite binary treestreams. This
   definition is analogous to the definition of streams provided in
   lecture. *)

type 'a tree = unit -> 'a tr
and 'a tr = Stem of 'a * 'a tree * 'a tree ;;

(*>* Problem 2.1.a *>*)
(* Write a function headt which takes an 'a treestream and returns the value
   at the root of the tree *)

let headt (t: 'a tree) : 'a =
  match t() with
  |Stem(a,_,_) -> a
;;

(*>* Problem 2.1.b *>*)
(* Write functions ltail and rtail which take a treestream and return its
   left and right subtrees respectively *)

let ltail (t: 'a tree) : 'a tree =
  match t() with
  |Stem(_,l,_) -> l
;;

let rtail (t: 'a tree) : 'a tree =
  match t() with
  |Stem(_,_,r) -> r
;;

(*>* Problem 2.1.c *>*)
(* Write a function mapt which takes takes a function f and maps it
   over the given treestream *)

let rec mapt (f: 'a -> 'b) (t: 'a tree) : 'b tree =
  fun () -> Stem(f (headt t), mapt f (ltail t), mapt f (rtail t))
;;

(*>* Problem 2.1.d *>*)
(* Write a function zipt which takes a function f and two treestreams
   t1 and t2 and combines them into one treestream. If x1 and x2 are the
   values at corresponding locations in t1 and t2 respectively, then
   the corresponding value in "zipt f t1 t2" should be "f x1 x2" *)

let rec zipt (f: 'a -> 'b -> 'c) (t1: 'a tree) (t2: 'b tree) : 'c tree =
  fun () -> Stem(f (headt t1) (headt t2), 
                     zipt f (ltail t1) (ltail t2),
                     zipt f (rtail t1) (rtail t2))
;;

(* Define a treestream of all ones *)

(*>* Problem 2.1.e *>*)
let rec onest () =
  Stem(1,onest,onest)
;;

(* Define a treestream in which each positive natural number appears
exactly once, and where the first few rows are 1; 2 3; 4 5 6 7,
etc. This should look something like the following

           1
         /   \
       2       3
     /   \   /   \
    4    5   6    7
   / \  / \ / \  / \
...
*)

(*>* Problem 2.1.f *>*)
let rec treenats () =
  Stem(1,mapt (( *) 2) treenats, mapt (fun x-> (x*2) + 1) treenats)
;;

(***************** Using the Lazy module ******************)
(* Here we provide an alternate implementation of streams using
   OCaml's lazy module. We recommend that you explore the
   documentation at
   http://caml.inria.fr/pub/docs/manual-ocaml/libref/Lazy.html

   In this portion, you will be reimplementing various functions that
   were defined in class.
*)

open Lazy

type 'a stream = Cons of 'a * 'a stream Lazy.t

let rec ones = Cons(1, lazy(ones));;

(*>* Problem 2.2.a *>*)
(* Implement the head function *)

let head (s:'a stream) : 'a =
  match s with
  |Cons(h,t) -> h
;;

(*>* Problem 2.2.b *>*)
(* Implement map *)

let rec map (f:'a -> 'b) (s:'a stream) : 'b stream =
  match s with
  |Cons(h,t) -> Cons(f h, lazy (map f (Lazy.force t)))
;;

(*>* Problem 2.2.c *>*)
(* Define nats *)

let rec nats = Cons(0, lazy(map ((+) 1) nats));;

(*>* Problem 2.2.d *>*)
(* Write a function nth, which returns the nth element of a
   stream. NOTE: the function nth should be zero-indexed. In other
   words, "nth 0 s" should be equivalent to "head s". *)

let rec nth (n:int) (s:'a stream) : 'a =
  match s with
  |Cons(h,t) -> 
    if n <= 0 then h
    else nth (n-1) (Lazy.force t)
;;

(*>* Problem 2.2.e *>*)
(* Now suppose we have two int streams s1 and s2 sorted in ascending
   order. We wish to merge these into a single stream s such that s is
   sorted in ascending order and has no duplicates. Implement this
   function. NOTE: This is not a simple merge function. You must
   REMOVE DUPLICATES *)

let rec merge (s1:int stream) (s2:int stream) : int stream =
  match s1,s2 with
  |Cons(h1,t1),Cons(h2,t2) ->
    if h1 > h2 then 
      Cons(h2, lazy (merge s1 (Lazy.force t2)))
    else if h1=h2 then 
      Cons(h1, lazy (merge (Lazy.force t1) (Lazy.force t2)))
    else
      Cons(h1, lazy (merge (Lazy.force t1) s2))   
;;

(* tests *)
let rec n3ts = Cons(1, lazy(map((+) 2) n3ts));;
let rec n2ts = Cons(0, lazy(map((+) 2) n2ts));;
let rec n0ts = merge n3ts n2ts;;
assert(nth 0 n0ts=0);;
assert(nth 1 n0ts=1);;
assert(nth 2 n0ts=2);;

(*>* Problem 2.2.f *>*)
(* What problems can we run into with this conception of "merge"? What
   if we were to run "merge ones ones"? Answer within the comment. *)

(* 
   Answer: Tricky Question. The only problem I can see with this is that if we go
    about merge ones ones, we'll just be iterating through an infinite list 
    without really modifying anything.
*)

(*>* Problem 2.2.g *>*)
(* Write a function "scale", which takes an integer "n" and an int
   stream "s", and multiplies each element of "s" by "n". *)

let scale s n = map(( *) n) s;;

(*>* Problem 2.2.h *>*)
(* Suppose we wish to create a stream of the positive integers "n" in
   increasing order such that any prime factor of "n" is either 3 or
   5. The first few numbers are 1, 3, 5, 9, 15, 25, 27, ... hopefully
   you get the idea. One way to do this is to run "filter" over
   "nats". But we can do better than that. *)

(* Let "selectivestream" denote the desired stream. Observe that "selectivestream" satisfies the
   following properties

   1. The elements of "scale S 3" are elements of "selectivestream"
   2. The elements of "scale S 5" are elements of "selectivestream"
   3. "selectivestream" is the minimal stream (sorted in increasing order) which
   contains "1" and satisfies the above properties

   Think about why properties 1-3 uniquely characterize "selectivestream".
*)

(* Use the above discussion and functions you've already written to
   give a simple definition for "selectivestream". This can be done quite
   elegantly. *)

let rec selectivestream = merge (scale nats 3) (scale nats 5);;

(*>* Problem 2.3 *>*)
(* Please give us an honest estimate of how long this part took 
 * you to complete.  We care about your responses and will use
 * them to help guide us in creating future assignments. *)
let minutes_spent : int = 35
