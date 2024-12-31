# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 08:36:35 2024

@author: R.N.GANDHI
"""

def alpha_beta(depth, node_index, maximizing_player, values, alpha, beta): # Base case: If the depth is 0, return the value at this node
if depth == 0:
return values[node_index] if maximizing_player:
max_eval = -math.inf # Start with a very small value
for i in range(2): # Assuming binary tree structure with two children
eval_value = alpha_beta(depth - 1, node_index * 2 + i, False, values, alpha, beta) max_eval = max(max_eval, eval_value)
alpha = max(alpha, eval_value) if beta <= alpha:
break # Beta cut-off return max_eval
else:
min_eval = math.inf # Start with a very large value
for i in range(2): # Assuming binary tree structure with two children
eval_value = alpha_beta(depth - 1, node_index * 2 + i, True, values, alpha, beta) min_eval = min(min_eval, eval_value)
beta = min(beta, eval_value) if beta <= alpha:
break # Alpha cut-off return min_eval
def main():
depth = int(input("Enter the depth of the tree: "))
num_nodes = 2 ** (depth + 1) - 1 # Number of nodes in a binary tree values = []

print(f"Enter the leaf node values for depth {depth}:")
for i in range(2 ** depth): # Leaf nodes are at the last level value = int(input(f"Enter value for leaf node {i+1}: ")) values.append(value)
alpha = -math.inf beta = math.inf
result = alpha_beta(depth, 0, True, values, alpha, beta) print(f"Optimal value (using Alpha-Beta Pruning): {result}")

if  name	== " main ": main()
