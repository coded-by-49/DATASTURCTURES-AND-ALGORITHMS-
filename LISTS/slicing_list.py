list = [10,20,30,40,50,60,70,80]

print(f"full slice {list[:]}\n")
print(f"half slice {list[:4]}\n") # half slice (start and stop)
print(f"reverse slice {list[-1:-9:-1]}")
# or 
print(f"reverse slice {list[::-1]}")

# you could either specify where you would want to stop either by incrementingt the end of the list
# or  you could leave it blank and that automatically does the job

#slicing in tuple

tup = (10,20,30,40,50,60)
print(f"tuples from 0 - end {tup[:4]}")