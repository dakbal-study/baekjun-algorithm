def shortest_palindrome_length(s):
    length = len(s)
    for i in range(length):
        if s[i:] == s[i:][::-1]:
            return length + i

s = input().strip()
print(shortest_palindrome_length(s))