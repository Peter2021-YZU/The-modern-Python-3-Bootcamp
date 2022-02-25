S1, S2 = (input().split())
s1 = int(S1)
s2 = int(S2)
count = int(1)

for i in range(1, s1, 2):
    print(str(".|."*i).center(s2, "-"))
print("WELCOME".center(s2, "-"))
for i in range(s1-2, -1, -2):
    print(str(".|."*i).center(s2, "-"))