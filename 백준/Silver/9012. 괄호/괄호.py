import sys

N = int(input())

for i in range(N):
    line = sys.stdin.readline().strip()
    # if line == '.' : break

    stack = []
    is_balanced = True

    for char in line:
        if char == "(" or char == "[":
            stack.append(char)
        elif char == ")":
            # if stack[-1] !='(' or not stack:
            if not stack or stack[-1] !='(':
                is_balanced = False
                break
            stack.pop()
        elif char == "]":
            if not stack or stack[-1] != "[":
                is_balanced = False
                break
            stack.pop()
    
    if is_balanced and not stack:
        print("YES")
    else:
        print("NO")
