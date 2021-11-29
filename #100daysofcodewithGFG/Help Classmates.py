class Solution:
    def help_classmate(self, arr, n):
        # Your code goes here
        # Return the list
        li = [-1]*n
        stack = [0]
        for i in range(1,n):
            while len(stack) and arr[i]<arr[stack[-1]]:
                temp = stack.pop()
                li[temp] = arr[i]
            stack.append(i)
        return li
