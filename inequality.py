a, b = 2, 6
print(a < b)
# True

a, b = 22, 6
print(a > b)
# True

a, b, c = 2, 3, 4
print(a < b < c)
# True

a, b, c = 6, 8, 8
print(a < b < c)
# False Cunki b ve c beraberdir bir sehv o biri duzude False eliyir.

d, f, g = 23, 45, 34
print(d < f > g)
# True

s, e, r =12,17,24
print(s<=e>=r)
# False e r-den boyuk deyil nede beraberdir, bir sehv ifadeni False edir.

s, e, r =12,17,24
print(s<=e<=r)
# True

x,y,u,g,r=2,5,12,15,18
print(x<y<=g>=u<r)
# True

j, q, n, l = 1, 2, 3, 3
print(j<q!=n==l)
# True

v = t = w = 3
print(v == t == w)
# True

h, u, k = 3, 4, 4
print(h!=u==k)
# True

h, u, k = 3, 4, 4
print(h==u!=k)
# False iki terefidde yanlisdir.

f, r, w, a = 12, 23, 67, 8
print(f > r and w > r and a == f and r != f)
# False 2,4 dogru 1,3 yanlisdir. True olmasi ucun butun berabersizlikler dogru olmalidir.

g, z, n, t = 22, 22, 33, 33
print(g == z and z < n and t > z and z != t and g<=n)
# True Butun berabersizlikler duzgun yerine yetirilib.

b,e,s,i=1,9,0,3
print(b==e or s!=i or e>i or b<=i)
# True 1. sehv olsa da cavab True cixir. False olmasi ucun her terefi sehv olmalidir

p, o, y, h, c = 2, 5, 8, 12, 12
print(p >= y or h < y or c == o or h != c or y >= c)
# False

d, r, y = 2, 3, 5
print(not (d < r or y != r))
# False moterizenin ici True olsa da not onu False eledi.

s, b, q, u = 5, 9, 14, 16
print(s <= q and u > b and b != s and q == u and s >= q)
# False
print(not (s <= q and u > b and b != s and q == u and s >= q))
# yuxarida False cixan cavabi Not True eledi.

a = input("a ededini daxil edin: ")
b = input("b ededini daxil edin: ")
c = input("c ededini daxil edin: ")
print(f"{a}x²+{b}x+{c}=0")

d = 274
print(f"yuzluk= {d//100}")

print(f"onluq= {d//10%10}")

print(f"teklik= {d%10}")

p=456
print(f"yuzluk= {p//100}")

print(f"onluq= {p//10%10}")

print(f"teklik= {p%10}")

w=987
print(f"yuzluk= {w//100}")

print(f"onluq= {w//10%10}")

print(f"teklik= {w%10}")

# Thank You For Your Attention ☻♥
