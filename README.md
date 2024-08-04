# Greedy Algorithms and Dynamic Programming

## Overview

This assignment focuses on implementing two algorithms to determine the best way to give change to a customer using a cash register system. The algorithms are a greedy algorithm and a dynamic programming algorithm.

## Comparison of Algorithms

I compared the performance of the greedy and dynamic programming algorithms based on their execution time and effectiveness for large sums:

- **Greedy Algorithm**:
  - **Advantages**: Fast and straightforward.
  - **Disadvantages**: Does not always find the optimal solution, especially for larger amounts.
  - **Use Case**: Suitable for scenarios where speed is more critical than the optimality of the solution.

- **Dynamic Programming Algorithm**:
  - **Advantages**: Always finds the optimal solution with the minimum number of coins.
  - **Disadvantages**: Slower compared to the greedy algorithm, especially for large amounts.
  - **Use Case**: Suitable for scenarios where finding the optimal solution is crucial.

## Conclusion

For small amounts, both greedy and dynamic programming algorithms are effective. However, for larger amounts, the dynamic programming approach is more reliable as it guarantees the minimum number of coins. While the greedy algorithm is faster, it may not always provide the best solution. 
