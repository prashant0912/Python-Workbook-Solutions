ls = []
while True:
    if len(ls) == 3:
        break
    n = int(input(("Enter the number:")))
    ls.append(n)

print("Minimum:", min(ls))
print("mid:", sum(ls) - (max(ls) + min(ls)))
print("Maximum:", max(ls))

