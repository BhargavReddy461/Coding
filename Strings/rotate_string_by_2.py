a = input()
b = input()
for i in range(2):
    k = b[0]
    b = b[1:]
    b = b+k
if a == b:
    print(True)
else:
    print(False)
