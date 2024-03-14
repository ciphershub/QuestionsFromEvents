This function, getWays, seems to implement a dynamic programming approach to solve the "coin change" problem. 
** Here's a breakdown of how it works:

1. The function takes two arguments:
- n: The target amount to make change for.
- c: A list of coin denominations available.

2. It initializes a list temp of size (n+1) filled with zeros. This list will store the number of ways to make change for each amount from 0 to n. temp[0] is set to 1 because there is only one way to make change for 0, which is to use no coins.

3. It iterates over each coin denomination x in the list c.

4. For each coin denomination x, it iterates over each amount y from x to n+1. For each amount y, it updates temp[y] by adding the value of temp[y-x]. This essentially means that it's adding the number of ways to make change for the amount y-x using the coin denomination x. By doing this, it builds up the number of ways to make change for each amount from smaller to larger amounts.

5. Finally, it returns temp[n], which represents the number of ways to make change for the target amount n.
