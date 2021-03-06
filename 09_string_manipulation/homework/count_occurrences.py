"""
Count Occurrences
Problem Description

Find number of occurrences of bob in the string A consisting of lowercase english alphabets.



Problem Constraints
1 <= |A| <= 1000


Input Format
The first and only argument contains the string A consisting of lowercase english alphabets.


Output Format
Return an integer containing the answer.


Example Input
Input 1:

  "abobc"
Input 2:

  "bobob"


Example Output
Output 1:

  1
Output 2:

  2


Example Explanation
Explanation 1:

  The only occurrence is at second position.
Explanation 2:

  Bob occures at first and third position.
"""

class Solution:
    # @param A : string
    # @return an integer
    count = 0
    def solve(self, A):
        for i in range(len(A)-2):
            if A[i] == 'b' and A[i+1] == 'o' and A[i+2] == 'b':
                self.count += 1
            continue
        return self.count

if __name__ == "__main__":
    obj = Solution()
    print(obj.solve("bobob"))