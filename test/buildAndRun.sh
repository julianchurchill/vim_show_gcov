#!/bin/sh

g++ -fprofile-arcs -ftest-coverage src/main.cpp -o test && ./test && gcov *.gcda
