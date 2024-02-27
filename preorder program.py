import preorder_function

R_true = {(1, 1), (1, 2), (2, 2), (2, 3), (1, 3), (3, 3)}

print(R_true)
print(preorder_function.is_preorder_relation(R_true))  
print(" ")

R_false = {(1, 1), (1, 2), (2, 2), (1, 3), (2, 3)}

print(R_false)
print(preorder_function.is_preorder_relation(R_false))  
