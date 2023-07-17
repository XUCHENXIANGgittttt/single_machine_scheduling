# Introduction
Constraint programming formulations for a single machine scheduling problem are provided in this repository. 

This project is aimed at providing a feasible (since optimal solution requires a large amount of solve time) production sequence for two identical machines to minimize makespan and changeover time. Since the two machines produce two different types of products and will not affect each other, this problem can be seen as a single machine scheduling problem.

Optimization models are formulated in Python and solved with Cplex by using DOcplex Python Modeling API.

# Features
* This project uses main_data.xlsx as an input, which includes every product's name, length, speed, demand quantity every week and other attributes.

* Users need to input the year and week where the prodution is scheduled and the max time given to the two machines.

* The output includes the feasible sequences and production time for each machine. Also, two excel files are created to store the solution.

# Acknowledgement
The data in main_data.xlsx is randomly generated.




