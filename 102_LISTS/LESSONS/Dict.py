# Dictionary comprehension
details = {
    "name": "fab",
    "height": 6.3,
    "spouse": None
}

l1 = [1,3,4,25]

d1 = {x:x**2 for x in l1}
print(d1)

l2 = [10,11,12,13,14,15]
d2 = {key:key**2 for key in l2 if key**2>150 }

print(d2)

d3 = {v:k for (k,v) in d2.items()}

print(f"This is the reverse of dz {d3}")