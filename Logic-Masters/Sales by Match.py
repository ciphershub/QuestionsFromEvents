** APPROACH 1 **

def sockMerchant(n, ar):
    pairs_count = [ar.count(i) // 2 for i in set(ar)]
    return sum(pairs_count)

**APPROACH 2**
def sockMerchant(n, ar):
    # Create an empty dictionary to store the count of each color of socks
    color_counts = {}
    
    # Loop through each color in the array
    for color in ar:
        # If the color is already in the dictionary, increment its count
        if color in color_counts:
            color_counts[color] += 1
        # Otherwise, initialize its count to 1
        else:
            color_counts[color] = 1
    
    # Initialize a variable to store the total number of pairs
    total_pairs = 0
    
    # Loop through the counts of each color in the dictionary
    for count in color_counts.values():
        # Calculate the number of pairs for each color by integer division by 2
        total_pairs += count // 2
    
    # Return the total number of pairs
    return total_pairs

# Example usage:
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
result = sockMerchant(len(ar), ar)
print("Total number of pairs:", result)
