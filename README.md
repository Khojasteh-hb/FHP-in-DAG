## FHP-in-DAG
FHP-in-DAG: Find Highest scoring Path in a labeled Directed Acyclic Graph


## Problem definition
Assume a labeled directed acyclic graph (DAG) in which nodes can have multiple ancestors and descendants and there is a single unique root node without any ancestor. In this DAG edge labels represent scores and range from zero to one. This code implements a solution to find highest scoring path, that is, the implementation finds the sequence of edges (path), for which the sum of edge labels is the highest of all possible paths.


## Unit test
A unit test is a test that checks a single component of code, usually modularized as a function, and ensures that it performs as expected.

https://docs.python.org/3/library/unittest.html

This python code was tested by unit tests to verify the correctness of the solution.


## Environment Settings
- Python version:  '3.9'

-  You just need to install the unittest library to run 'test_find_longest_path.py'  

## About examples

5<-(this is number of vertices) 7 <- (this is number of edges)  

1 2 7 <-(these are in the form: from vertex, to vertex, weight)  
1 3 10  
2 4 8  
2 5 3  
3 4 5  
3 5 10  
4 5 5  

The examples namely 'inSample_' are the normal inputs and the ones namely 'test_' are to show program can print approprite message for abnormal inuts (such as weight would be negative or would not be in range and so on.) 

## To run the code 'find_longest_path.py'

- Change directory to the code path by command:

  cd /path/to

- Run the code by command:

  cat inSample_1.txt | python3 find_longest_path.py


## To run the code 'test_find_longest_path.py'

- Change directory to the code path by command:

  cd /path/to

- Run the code by command:
  
  python3 test_find_longest_path.py

![Screenshot 2022-10-24 084804](https://user-images.githubusercontent.com/72028345/197453787-b7b1221d-e9d1-4e4c-9cf5-bb0ebb0ad1b6.png)

# Contact
If you have any questions, do not hesitate to contact me by `khojasteh.hb@gmail.com`, I will be happy to assist.

