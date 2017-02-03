# Advanced Data Structures & Algorithms with Python

## Course Schedule

**Course Dates:** Monday, January 23 – Friday, March 3, 2017 (6 weeks)

**Class Times:** Monday, Wednesday, Friday 1–3pm (17 class sessions)

### Class 1: Monday, January 23 – Exponents & Number Bases

**Topics:**
  - review exponents, logarithms
  - [number bases slides](NumberBases.pdf): decimal, binary, hexadecimal
  - [negative integer representations](https://en.wikipedia.org/wiki/Signed_number_representations): signed magnitude, ones' complement, two's complement

**Challenges:**
  - practice number base conversions on [worksheet](NumberBasesWorksheet.pdf)
  - implement base conversion functions for positive numbers using [starter code](bases.py) and [unit tests](test_bases.py)
  - stretch: implement base conversion for negative numbers
  - stretch: implement base conversion for fractional numbers


### Class 2: Wednesday, January 25 – Recursion & Search Algorithms

**Topics:**
  - compare iteration and [recursion](recursion.py) with factorial function
  - searching algorithms: linear search and [binary search](https://en.wikipedia.org/wiki/Binary_search_algorithm)
  - review [algorithm complexity analysis](AlgorithmAnalysis.pdf)

**Challenges:**
  - implement iterative factorial function using [starter code](recursion.py) and [unit tests](test_recursion.py)
  - implement recursive linear and binary search algorithms using [starter code](search.py) and [unit tests](test_search.py)
  - annotate functions with complexity analysis
  - stretch: implement [permutation](https://en.wikipedia.org/wiki/Permutation) and [combination](https://en.wikipedia.org/wiki/Combination) functions


###  Class 3: Friday, January 27 – String Algorithms

**Topics:**
  - [string searching](https://en.wikipedia.org/wiki/String_searching_algorithm), [palindromes](https://en.wikipedia.org/wiki/Palindrome), [anagrams](https://en.wikipedia.org/wiki/Anagram)

**Challenges:**
  - implement string searching function (try multiple approaches)
  - implement iterative and recursive palindrome checking functions using [starter code](strings.py) and [unit tests](test_strings.py)
  - annotate functions with complexity analysis
  - stretch: implement iterative and recursive anagram generating functions

**Project:**
  - [phone call routing](https://www.dropbox.com/sh/tj6ppp6uwf12cce/AADje96PJhfsIXJEtP1OjwjFa): implement phone number prefix matching
  - annotate functions with complexity analysis


### Class 4: Monday, January 30 – List, Stack & Queue

**Topics:**
- compare [abstract data types][adt] and [concrete data structures][ds]
- abstract data types: [list], [stack], [queue], [deque]
- concrete data structures: [array], [dynamic array (resizable array, vector)][dynamic array], [linked list]
- watch Make School's video lectures: [linked list][ms video linked list], [stack and queue][ms video stack queue]
- play with interactive visualizations: [linked list, stack, queue, deque][visualgo list]

**Challenges:**
- implement constant-time length function on linked list using [starter code](linkedlist.py) and [unit tests](test_linkedlist.py)
- implement stack with dynamic array and linked list using [starter code](stack.py) and [unit tests](test_stack.py)
- implement queue with dynamic array and linked list using [starter code](queue.py) and [unit tests](test_queue.py)
- annotate functions with complexity analysis
- stretch: implement deque with doubly linked list

[adt]: https://en.wikipedia.org/wiki/Abstract_data_type
[ds]: https://en.wikipedia.org/wiki/Data_structure
[list]: https://en.wikipedia.org/wiki/List_(abstract_data_type)
[stack]: https://en.wikipedia.org/wiki/Stack_(abstract_data_type)
[queue]: https://en.wikipedia.org/wiki/Queue_(abstract_data_type)
[deque]: https://en.wikipedia.org/wiki/Double-ended_queue
[array]: https://en.wikipedia.org/wiki/Array_data_structure
[dynamic array]: https://en.wikipedia.org/wiki/Dynamic_array
[linked list]: https://en.wikipedia.org/wiki/Linked_list
[ms video linked list]: https://www.youtube.com/watch?v=3WWuf4H61Nk
[ms video stack queue]: https://www.youtube.com/watch?v=AXWnk4gege4
[visualgo list]: https://visualgo.net/list


### Class 5: Wednesday, February 1 – Set, Map, & Hash Table

**Topics:**
- abstract data types: [set], [multiset (bag)][multiset], [map (dictionary, associative array)][map]
- concrete data structures: [hash table]
- watch Make School's video lecture: [hash table][ms video hash table]
- play with interactive visualizations: [hash table][visualgo hash table]
- bonus abstract data type: [circular buffer]

**Challenges:**
- implement set with hash table
- implement automatic resizing of hash table
- annotate functions with complexity analysis
- stretch: implement [set operations] union, intersection, difference, subset
- stretch: implement circular buffer with dynamic array and linked list

[set]: https://en.wikipedia.org/wiki/Set_(abstract_data_type)
[set operations]: https://en.wikipedia.org/wiki/Set_(abstract_data_type)#Operations
[multiset]: https://en.wikipedia.org/wiki/Set_(abstract_data_type)#Multiset
[map]: https://en.wikipedia.org/wiki/Associative_array
[hash table]: https://en.wikipedia.org/wiki/Hash_table
[circular buffer]: https://en.wikipedia.org/wiki/Circular_buffer
[ms video hash table]: https://www.youtube.com/watch?v=nLWXJ6IDKmQ
[visualgo hash table]: https://visualgo.net/hashtable


### Class 6: Friday, February 3 – Trees & Traversals

**Topics:**
- [tree], [binary search tree], [n-ary tree], operations
- [tree traversal]: pre-order, post-order, in-order, level-order
- watch Make School's video lectures: [tree][ms video tree], [tree traversal][ms video tree traversal]
- play with interactive visualizations: [binary search tree][visualgo bst]

**Challenges:**
- implement binary search tree with node objects
- implement search, insert, delete binary search tree operations
- implement iterative and recursive binary search tree traversals
- implement map (dictionary) with binary search tree
- annotate functions with complexity analysis
- stretch: implement binary search tree with singly linked list
- stretch: implement n-ary search tree with dynamic array

[tree]: https://en.wikipedia.org/wiki/Tree_%28data_structure%29
[binary search tree]: https://en.wikipedia.org/wiki/Binary_search_tree
[n-ary tree]: https://en.wikipedia.org/wiki/K-ary_tree
[tree traversal]: https://en.wikipedia.org/wiki/Tree_traversal
[ms video tree]: https://www.youtube.com/watch?v=Yr3y78d2KYI
[ms video tree traversal]: https://www.youtube.com/watch?v=Qd8dKFaRu9I
[visualgo bst]: https://visualgo.net/bst


## Working with this GitHub repository

This repository (located at `https://github.com/MakeSchool-18/Data-Structures`) is the course's _origin_ repository which will contain course materials including links, slides, and challenges.
Note that you cannot commit or push to the origin repository.
However, you can _fork_ it to maintain your own version of it and push your code there. Here's an overview of what your repository setup should look like:

![Repository Overview](repository-overview.png "Repository Overview")

Follow these steps to set up your own course repository:

1. Clone this repository on your computer:
`git clone git@github.com:MakeSchool-18/Data-Structures.git`

2. Fork this repository on GitHub to create your own version of this repo on your GitHub account, which should also be named `Data-Structures`

3. Add your GitHub repository as a _remote_ to the local one on your computer (note: you need to give a name to the remote, e.g. your first name):
`git remote add <first-name> git@github.com:<github-user>/Data-Structures.git`

4. Link the local repo to your remote GitHub repo:
`git push -u <first-name> master`

5. When you want to access new course materials, just pull from the origin remote repo:
`git pull origin master`

6. When you've completed a challenge and want to share it for code review, commit your work and push it to your own remote repo with:
`git push`
