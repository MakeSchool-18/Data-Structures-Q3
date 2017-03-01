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

**Resources:**
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


### Class 5: Wednesday, February 1 – Set, Map & Hash Table

**Topics:**
- abstract data types: [set], [multiset (bag)][multiset], [map (dictionary, associative array)][map]
- concrete data structures: [hash table]
- bonus abstract data type: [circular buffer]

**Resources:**
- watch Make School's video lecture: [hash table][ms video hash table]
- play with interactive visualizations: [hash table][visualgo hash table]

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


### Class 6: Friday, February 3 – Trees

**Topics:**
- [tree], [binary search tree], operations

**Resources:**
- watch Make School's video lecture: [tree][ms video tree]
- play with interactive visualizations: [binary search tree][visualgo bst]

**Challenges:**
- implement binary search tree with node objects
- implement search, insert, delete binary search tree operations
- annotate functions with complexity analysis
- stretch: implement binary search tree with singly linked list

**Project:**
- [trees and mazes] tutorial on Make School's [Online Academy]

[tree]: https://en.wikipedia.org/wiki/Tree_%28data_structure%29
[binary search tree]: https://en.wikipedia.org/wiki/Binary_search_tree
[ms video tree]: https://www.youtube.com/watch?v=Yr3y78d2KYI
[visualgo bst]: https://visualgo.net/bst

[trees and mazes]: http://make.sc/oa-trees-and-mazes
[Online Academy]: https://www.makeschool.com/academy


### Class 7: Monday, February 6 – Tree Traversals & Self-Balancing Trees

**Topics:**
- [tree traversals]: pre-order, post-order, in-order, level-order
- [self-balancing trees] with [rotations]: [AVL tree], [splay tree], [red-black tree]

**Resources:**
- watch Make School's video lecture: [tree traversals][ms video tree traversals]

**Challenges:**
- implement iterative and recursive binary search tree traversals
- implement map (dictionary) with binary search tree
- annotate functions with complexity analysis
- stretch: implement AVL tree or splay tree with insert and search operations

[tree traversals]: https://en.wikipedia.org/wiki/Tree_traversal
[ms video tree traversals]: https://www.youtube.com/watch?v=Qd8dKFaRu9I
[self-balancing trees]: https://en.wikipedia.org/wiki/Self-balancing_binary_search_tree
[rotations]: https://en.wikipedia.org/wiki/Tree_rotation
[AVL tree]: https://en.wikipedia.org/wiki/AVL_tree
[splay tree]: https://en.wikipedia.org/wiki/Splay_tree
[red-black tree]: https://en.wikipedia.org/wiki/Red%E2%80%93black_tree


### Class 8: Wednesday, February 8 – More Self-Balancing Trees

**Topics:**
- [n-ary tree]
- [self-balancing trees] with multiple keys: [2-3 tree], [B-tree]
- [space-partitioning] trees: [quadtree], [octree], [k-d tree]

**Challenges:**
- implement 2-3 tree with insert and search operations
- annotate functions with complexity analysis
- stretch: implement n-ary search tree using dynamic array of siblings
- stretch: implement B-tree or k-d tree with insert and search operations

[n-ary tree]: https://en.wikipedia.org/wiki/K-ary_tree
[2-3 tree]: https://en.wikipedia.org/wiki/2%E2%80%933_tree
[B-tree]: https://en.wikipedia.org/wiki/B-tree
[space-partitioning]: https://en.wikipedia.org/wiki/Space_partitioning
[quadtree]: https://en.wikipedia.org/wiki/Quadtree
[octree]: https://en.wikipedia.org/wiki/Octree
[k-d tree]: https://en.wikipedia.org/wiki/K-d_tree


### Class 9: Friday, February 10 – Iterative Sorting Algorithms

**Topics:**
- iterative [comparison sorting]: [bubble], [selection], [insertion]
- [integer sorting]: [counting], [bucket], [radix]

**Resources:**
- watch [animations] and [this video] of sorting algorithms to see patterns
- play with step-by-step [interactive animations] of sorting algorithms

**Challenges:**
- implement bubble, selection, and insertion sorts
- implement counting and bucket sorts
- annotate functions with complexity analysis
- stretch: implement insertion sort using binary search
- stretch: implement [cocktail shaker] or [Shell] sort

**Project:**
- [sorting algorithms] with real-world data on Make School's [Online Academy]

[comparison sorting]: https://en.wikipedia.org/wiki/Comparison_sort
[bubble]: https://en.wikipedia.org/wiki/Bubble_sort
[selection]: https://en.wikipedia.org/wiki/Selection_sort
[insertion]: https://en.wikipedia.org/wiki/Insertion_sort

[integer sorting]: https://en.wikipedia.org/wiki/Integer_sorting
[counting]: https://en.wikipedia.org/wiki/Counting_sort
[bucket]: https://en.wikipedia.org/wiki/Bucket_sort
[radix]: https://en.wikipedia.org/wiki/Radix_sort
[cocktail shaker]: https://en.wikipedia.org/wiki/Cocktail_shaker_sort
[Shell]: https://en.wikipedia.org/wiki/Shellsort

[animations]: https://www.toptal.com/developers/sorting-algorithms/
[interactive animations]: https://www.cs.usfca.edu/~galles/visualization/ComparisonSort.html
[this video]: https://www.youtube.com/watch?v=jHPexHsDxwQ

[sorting algorithms]: http://make.sc/oa-sorting-algorithms


### Class 10: Monday, February 13 – Divide-and-Conquer Recursion

**Topics:**
- [divide-and-conquer]&nbsp;[recursion]: divide, conquer, combine
- revisit [binary search] to see how it divides and conquers
- [merge algorithm] and [merge sort]

**Challenges:**
- implement [merge sort] with a separate [merge algorithm]
- implement [tree sort] with an appropriate [search tree]
- annotate functions with complexity analysis
- stretch: implement [radix sort][radix] for integers and/or strings

**Project:**
- continue [sorting algorithms] with real-world data

[divide-and-conquer]: https://en.wikipedia.org/wiki/Divide_and_conquer_algorithm
[recursion]: https://en.wikipedia.org/wiki/Recursion_(computer_science)
[binary search]: https://en.wikipedia.org/wiki/Binary_search_algorithm
[merge algorithm]: https://en.wikipedia.org/wiki/Merge_algorithm
[merge sort]: https://en.wikipedia.org/wiki/Merge_sort
[tree sort]: https://en.wikipedia.org/wiki/Tree_sort
[search tree]: https://en.wikipedia.org/wiki/Search_tree


### Class 11: Wednesday, February 15 – Recursive Sorting Algorithms

**Topics:**
- [recursive algorithm analysis] with trees, [recurrence relations], [master theorem]
- partition algorithm and [quick sort]
- [stable sorting] and [adaptive sorting]

**Resources:**
- watch these cute robot video animations: [quick sort][video quick sort], [merge sort vs. quick sort][video merge quick sort]

**Challenges:**
- implement stable quick sort with a separate partition algorithm
- annotate functions with complexity analysis

[recursive algorithm analysis]: AlgorithmAnalysisRecursive.pdf
[recurrence relations]: https://en.wikipedia.org/wiki/Recurrence_relation
[master theorem]: https://en.wikipedia.org/wiki/Master_theorem
[quick sort]: https://en.wikipedia.org/wiki/Quicksort
[stable sorting]: https://en.wikipedia.org/wiki/Sorting_algorithm#Stability
[adaptive sorting]: https://en.wikipedia.org/wiki/Adaptive_sort
[video quick sort]: https://www.youtube.com/watch?v=aXXWXz5rF64
[video merge quick sort]: https://www.youtube.com/watch?v=es2T6KY45cA


### Class 12: Friday, February 17 – Priority Queue & Heap

**Topics:**
- [priority queue] abstract data type
- [heap] data structure, [binary heap] representations
- [heap sort], compare to [insertion] and [selection] sort

**Resources:**
- watch Make School's [video lecture][ms video heap] and review [slides on heaps][ms slides heap]
- watch this cute robot video animation: [heap and heap sort][video heap sort]
- play with interactive visualizations: [heap][visualgo heap]
- read about [sorting algorithms implemented with priority queue][priority queue sorting]

**Challenges:**
- implement binary min heap with dynamic array using [starter code](heap.py) and [unit tests](test_heap.py)
- implement heap sort with binary heap
- implement priority queue with binary heap
- implement priority queue with binary search tree
- annotate functions with complexity analysis
- stretch: implement stack with priority queue
- stretch: generalize binary heap with min or max initialization option

[priority queue]: https://en.wikipedia.org/wiki/Priority_queue
[heap]: https://en.wikipedia.org/wiki/Heap_(data_structure)
[binary heap]: https://en.wikipedia.org/wiki/Binary_heap
[heap sort]: https://en.wikipedia.org/wiki/Heapsort

[ms slides heap]: Heaps.pdf
[ms video heap]: https://www.youtube.com/watch?v=eBGgEEXnbuk
[video heap sort]: https://www.youtube.com/watch?v=H5kAcmGOn4Q
[visualgo heap]: https://visualgo.net/heap
[priority queue sorting]: https://en.wikipedia.org/wiki/Priority_queue#Equivalence_of_priority_queues_and_sorting_algorithms


### Class 13: Wednesday, February 22 – Graphs

**Topics:**
- [graph abstract data type][graph adt]
- [graph types]: [directed]/undirected, weighted/unweighted, simple/[multigraph]
- [graph applications]: computer networking, social networking, airplane flight routing, map routing, search engines ([PageRank]), dependency planning, etc.
- [graph representations]: object references, edge list, [incidence matrix], [adjacency matrix], [adjacency list], adjacency map

**Resources:**
- play with interactive visualizations: [graph types and representations][visualgo graph]

**Project:**
- collect data set of social network, airplane routes, or your choice
- implement graph with appropriate representation for that data set

[graph adt]: https://en.wikipedia.org/wiki/Graph_(abstract_data_type)
[graph types]: https://en.wikipedia.org/wiki/Graph_(discrete_mathematics)#Types_of_graphs
[directed]: https://en.wikipedia.org/wiki/Directed_graph
[multigraph]: https://en.wikipedia.org/wiki/Multigraph
[graph applications]: https://en.wikipedia.org/wiki/Graph_theory#Applications
[PageRank]: https://en.wikipedia.org/wiki/PageRank
[graph representations]: https://en.wikipedia.org/wiki/Graph_(abstract_data_type)#Representations
[incidence matrix]: https://en.wikipedia.org/wiki/Incidence_matrix
[adjacency matrix]: https://en.wikipedia.org/wiki/Adjacency_matrix
[adjacency list]: https://en.wikipedia.org/wiki/Adjacency_list
[graph traversals]: https://en.wikipedia.org/wiki/Graph_traversal
[depth-first search]: https://en.wikipedia.org/wiki/Depth-first_search
[breadth-first search]: https://en.wikipedia.org/wiki/Breadth-first_search

[visualgo graph]: https://visualgo.net/graphds


### Class 14: Friday, February 24 – Graph Traversals & Spanning Trees

**Topics:**
- [graph traversals]: [depth-first search], [breadth-first search]
- graph [connectivity], [connected components], [strongly connected components]
- graph [spanning trees], [minimum spanning trees]:
    - [Prim's algorithm]
    - [Kruskal's algorithm]
- bonus data structure: [trie (prefix/radix tree)][trie]

**Resources:**
- play with interactive visualizations: [graph traversals][visualgo traversals], [minimum spanning tree][visualgo mst]

**Graph Project:**
- implement graph traversals: depth-first search, breadth-first search
- implement an algorithm to find connected components on your graph data set
- implement an algorithm to find a minimum spanning tree on your graph data set
- annotate functions with complexity analysis

**Trie Project:**
- implement trie with insert and prefix search operations
- revisit [phone call routing] scenarios 3, 4, and 5 with trie
- annotate functions with complexity analysis

[connectivity]: https://en.wikipedia.org/wiki/Connectivity_(graph_theory)
[connected components]: https://en.wikipedia.org/wiki/Connected_component_(graph_theory)
[strongly connected components]: https://en.wikipedia.org/wiki/Strongly_connected_component
[disjoint-set]: https://en.wikipedia.org/wiki/Disjoint-set_data_structure
[spanning trees]: https://en.wikipedia.org/wiki/Spanning_tree
[minimum spanning trees]: https://en.wikipedia.org/wiki/Minimum_spanning_tree
[Prim's algorithm]: https://en.wikipedia.org/wiki/Prim%27s_algorithm
[Kruskal's algorithm]: https://en.wikipedia.org/wiki/Kruskal%27s_algorithm

[visualgo traversals]: https://visualgo.net/dfsbfs
[visualgo mst]: https://visualgo.net/mst

[trie]: https://en.wikipedia.org/wiki/Trie
[phone call routing]: http://make.sc/db-phone-call-routing


### Class 15: Monday, February 27 – Graph Algorithms

**Topics:**
- [shortest path problem]:
    - [A* search algorithm]
    - [Dijkstra's algorithm]
    - [Bellman–Ford algorithm]
    - [Floyd–Warshall algorithm]
- [maximum flow problem]:
    - [Ford–Fulkerson algorithm]
    - [Edmonds–Karp algorithm]
    - [max-flow min-cut theorem]
- [matching problem], [assignment problem]

**Resources:**
- play with interactive visualizations: [shortest path][visualgo shortest path], [max flow][visualgo max flow], [matching][visualgo matching]

**Graph Project:**
- implement an algorithm to find a shortest path or maximum flow on your graph data set
- annotate functions with complexity analysis

[shortest path problem]: https://en.wikipedia.org/wiki/Shortest_path_problem
[A* search algorithm]: https://en.wikipedia.org/wiki/A*_search_algorithm
[Dijkstra's algorithm]: https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
[Bellman–Ford algorithm]: https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm
[Floyd–Warshall algorithm]: https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm

[maximum flow problem]: https://en.wikipedia.org/wiki/Maximum_flow_problem
[Ford–Fulkerson algorithm]: https://en.wikipedia.org/wiki/Ford%E2%80%93Fulkerson_algorithm
[Edmonds–Karp algorithm]: https://en.wikipedia.org/wiki/Edmonds%E2%80%93Karp_algorithm
[max-flow min-cut theorem]: https://en.wikipedia.org/wiki/Max-flow_min-cut_theorem
[matching problem]: https://en.wikipedia.org/wiki/Matching_(graph_theory)
[assignment problem]: https://en.wikipedia.org/wiki/Assignment_problem

[visualgo shortest path]: https://visualgo.net/sssp
[visualgo max flow]: https://visualgo.net/maxflow
[visualgo matching]: https://visualgo.net/matching


### Class 16: Wednesday, March 1 – Dynamic Programming

**Topics:**
- [combinatorial optimization], [greedy algorithms]
- revisit [recursion] with [dynamic programming]

**Challenges:**
- implement recursive function to solve rod-cutting problem
- implement dynamic programming function to solve rod-cutting problem
- annotate functions with complexity analysis

**Resources:**
- play with interactive visualizations: [recursion and dynamic programming][visualgo recursion]
- read about [dynamic programming][wikibooks dp] and [greedy algorithms][wikibooks greedy] on WikiBooks

[combinatorial optimization]: https://en.wikipedia.org/wiki/Combinatorial_optimization
[greedy algorithms]: https://en.wikipedia.org/wiki/Greedy_algorithm
[dynamic programming]: https://en.wikipedia.org/wiki/Dynamic_programming

[wikibooks greedy]: https://en.wikibooks.org/wiki/Algorithms/Greedy_Algorithms
[wikibooks dp]: https://en.wikibooks.org/wiki/Algorithms/Dynamic_Programming
[visualgo recursion]: https://visualgo.net/recursion


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
