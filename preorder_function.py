def is_preorder_relation(R):
    # Check if R is reflexive
    reflexive = all((x, x) in R for x in set(y for x, y in R))
    
    # Check if R is transitive
    transitive = all((a, c) in R for a in set(x for x, y in R) 
                     for b in set(y for x, y in R) 
                     for c in set(z for y, z in R) if (a, b) in R and (b, c) in R)
    
    # If R is reflexive and transitive, it is a preorder relation
    return reflexive and transitive

