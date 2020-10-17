square = {f"square of {i}":i**2  for i in range(1,11)}
for k,v in square.items():
    print(f"{k} : {v}")

name = 'Sagar'
counter = {i:i.count(i) for i in name}
print(counter)
