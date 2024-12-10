# Puckett-Monahan-CS452-Final

Running test cases:
Naming convention -> test_case# where # is the maximum clique in the graph
                  -> test_case#v signifies that the correct maximum clique is not the entire graph to introduce edges/vertices that aren't part of the clique

cd into the code_solution directory
cd code_solution/

give yourself execute permission for the run_test_cases.sh
chmod +x run_test_cases.sh

then run the shell script
./run_test_cases.sh

This should run all the test cases for both the bron-kerbosch and approximation algorithms
Additionally, it will run the brute_force_sol with the test_case26 file and that will run for 14 to 20 minutes

If there is an error in the script ie. "command not found python"; please edit the shell script to say

python3 instead of python for every run command (issue we ran into with our laptops)

ie. "python bron-kerbosch.py test_case4" would become "python3 bron-kerbosch.py test_case4"

To run the variance script:
cd into the code-solution directory

give yourself execute permission for the variance_script.sh
chmod +x variance_script.sh

then run the shell script
./variance_script.sh

You may run into the same problem in which case please make the same edit.