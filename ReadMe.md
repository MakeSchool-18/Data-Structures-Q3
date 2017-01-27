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
  - string searching, [palindromes](https://en.wikipedia.org/wiki/Palindrome), [anagrams](https://en.wikipedia.org/wiki/Anagram)

**Challenges:**
  - implement string searching function (try multiple approaches)
  - implement iterative and recursive palindrome checking functions using [starter code](strings.py) and [unit tests](test_strings.py)
  - annotate functions with complexity analysis
  - stretch: implement iterative and recursive anagram generating functions

**Project:**
  - [phone call routing](https://www.dropbox.com/sh/tj6ppp6uwf12cce/AADje96PJhfsIXJEtP1OjwjFa): implement phone number prefix matching
  - annotate functions with complexity analysis


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
