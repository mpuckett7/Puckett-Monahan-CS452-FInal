#!/bin/bash

# Script to run test_cases for both exact and approximate
# Written  By: Mason Puckett and Annabelle Monahan

echo "==== Test Case 4 ===="
echo "Exact Solution: bron-kerbosch"
python bron-kerbosch.py test_case4
echo
echo
echo "Approximation: Fiege"
python approximation.py test_case4
echo
echo

echo "==== Test Case 6 ===="
echo "Exact Solution: bron-kerbosch"
python bron-kerbosch.py test_case6
echo
echo
echo "Approximation: Fiege"
python approximation.py test_case6
echo
echo

echo "==== Test Case 6v ===="
echo "Exact Solution: bron-kerbosch"
python bron-kerbosch.py test_case6v
echo
echo
echo "Approximation: Fiege"
python approximation.py test_case6v
echo
echo

echo "==== Test Case 10 ===="
echo "Exact Solution: bron-kerbosch"
python bron-kerbosch.py test_case10
echo
echo
echo "Approximation: Fiege"
python approximation.py test_case10
echo
echo

echo "==== Test Case 10v ===="
echo "Exact Solution: bron-kerbosch"
python bron-kerbosch.py test_case10v
echo
echo
echo "Approximation: Fiege"
python approximation.py test_case10v
echo
echo

echo "==== Test Case 16 ===="
echo "Exact Solution: bron-kerbosch"
python bron-kerbosch.py test_case16
echo
echo
echo "Approximation: Fiege"
python approximation.py test_case16
echo
echo

echo "==== Test Case 16v ===="
echo "Exact Solution: bron-kerbosch"
python bron-kerbosch.py test_case16v
echo
echo
echo "Approximation: Fiege"
python approximation.py test_case16v
echo
echo

echo "==== Test Case 20 ===="
echo "Exact Solution: bron-kerbosch"
python bron-kerbosch.py test_case20
echo
echo
echo "Approximation: Fiege"
python approximation.py test_case20
echo
echo

echo "==== Test Case 20v ===="
echo "Exact Solution: bron-kerbosch"
python bron-kerbosch.py test_case20v
echo
echo
echo "Approximation: Fiege"
python approximation.py test_case20v
echo
echo

echo "==== Test Case 22 ===="
echo "Exact Solution: bron-kerbosch"
python bron-kerbosch.py test_case22
echo
echo
echo "Approximation: Fiege"
python approximation.py test_case22
echo
echo

echo "==== Test Case 25 ===="
echo "Exact Solution: bron-kerbosch"
python bron-kerbosch.py test_case25
echo
echo
echo "Approximation: Fiege"
python approximation.py test_case25
echo
echo

echo "==== Test Case 26 ===="
echo "Exact Solution: bron-kerbosch"
python bron-kerbosch.py test_case26
echo
echo
echo "Approximation: Fiege"
python approximation.py test_case26
echo
echo

echo "==== Twenty Minute Test Case ===="
echo "-> Uses brute_force_sol.py and not bron-kerbosch"
python brute_force_sol.py test_case26
echo
echo
