"""
Compute area of rectangle

Given the length and breadth of a rectangle, print area of the rectangle.

Input Format

First and only line of input contains two positive integers L - length of the rectangle and B - breadth of the rectangle.

Constraints

1 <= L, B <=109

Output Format

Print area of the given rectangle.

Sample Input 0

5 8
Sample Output 0

40
Explanation 0

Self Explanatory

"""

L,B=[int(x) for x in input().split()]
print(L*B)