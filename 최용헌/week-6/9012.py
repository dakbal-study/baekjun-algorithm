n = int(input())


for _ in range(n):
    s = input()
    flag = "YES"

    if s[0] == ")":
        print("NO")
        continue

    lis = [s[0]]

    for i in range(1, len(s)):
        if len(lis) == 0:
            if s[i] == ")":
                flag = "NO"
                break
            else:
                lis.append("(")
        else:
            if s[i] == "(":
                lis.append("(")
            else:
                lis.pop()

    if len(lis) == 0:
        print(flag)
    else:
        print("NO")




