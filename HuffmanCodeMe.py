import math

def huffman_code(probabilities):
    # Create a list of tuples (probability, letter)
    nodes = [(p, i) for i, p in enumerate(probabilities)]
    
    # Combine nodes with lowest probabilities until only one node remains
    while len(nodes) > 1:
        # Sort the nodes by increasing probability
        nodes.sort(key=lambda t:t[0])
        # Combine the two nodes with lowest probabilities
        p1, i1 = nodes.pop(0)
        p2, i2 = nodes.pop(0)
        nodes.append((p1+p2, (i1, i2)))
    
    # create the Huffman tree and  the code table 
    code_table = {}
    def Check_Nodes(node, code):
        if isinstance(node, int):
            code_table[node] = code
        else:
            Check_Nodes(node[0], code+'0')
            Check_Nodes(node[1], code+'1')
    Check_Nodes(nodes[0][1], '')
    
    # Calculate the code efficiency and redundancy
    code_length = sum(p * len(code_table[i]) for i, p in enumerate(probabilities))
    entropy = sum(-p * math.log2(p) for p in probabilities)
    efficiency = round(entropy / code_length *100,1)
    redundancy = round(100 - efficiency,1) 
    print("CodeLength(R)= ",round(code_length,3),"  Entropy(H) = ",round(entropy,2))
    return code_table, efficiency, redundancy


# User Inputs and Outputs

letters = ['A', 'B', 'C', 'D', 'E', 'F']
probabilities = [0.24, 0.1, 0.04, 0.5, 0.01, 0.11]
code_table, efficiency, redundancy = huffman_code(probabilities)


# Print the Huffman code table for each letter
print("Huffman code table:")
for i, letter in enumerate(letters):
    print(letter, ":", code_table[i])

# Print the code efficiency and redundancy
print("Code efficiency (H/R)= ",  efficiency,"%")
print("Redundancy:", redundancy,"%")


# Encode a given word using the generated Huffman code table
word = "FACE"
encoded_word = ''.join(code_table[letters.index(c)] for c in word)
print("Encoded word:", encoded_word)
