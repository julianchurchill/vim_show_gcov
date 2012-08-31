#!/bin/sh

g++ -fprofile-arcs -ftest-coverage src/main.cpp -o main_test && ./main_test && gcov *.gcda
