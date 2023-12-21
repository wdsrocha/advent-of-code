from math import sqrt, floor, ceil

t = int("".join([x for x in input().split(" ") if x.isnumeric()]))
d = int("".join([x for x in input().split(" ") if x.isnumeric()]))
print(t, d)


# bhaskara
def get_roots(a, b, c):
    delta = (b * b) - (4 * a * c)
    r0 = (-b - sqrt(delta)) / (2 * a)
    r1 = (-b + sqrt(delta)) / (2 * a)

    return min(r0, r1), max(r0, r1)


ans = 1
r0, r1 = get_roots(-1, t, -d)

l = floor(r0 + 1)
r = ceil(r1 - 1)

print(l, r, r - l + 1)
ans *= r - l + 1

print(ans)
