## Parallel Computing Matrix Multiply Assignment

This repository contains some basic Python utilities for
matrix operations. This is also the repository where
you will submit the assignment.

Once completed the repository should contain your code,
a short report, and any instructions needed to run your
code.

## How to Run MatrixMultiply.py

MatrixMultiply.py tests and runs both the serial and parallel algorithm for
multiplying matrices. To use the program run python3 ./MatrixMultiply.py with the following argument options:
    -e runs the serial algorithm
    -p runs the parallel algorithm
    -s (followed by integer) size of the square 2d arrays, default is 700
    -v (followed by integer) value, default is 1
    -f (followed by String) file name, where the result matrix will be stored. Default is output.txt
Example: student@linux:~/python3 MatrixMultiply.py -p -n 4 -s 300
