
num = 3
if num > 0:
    print(num, "is a positive number.")
print("This is always printed.")

num = -1
if num > 0:
    print(num, "is a positive number.")
print("This is also always printed.")


x=45
if x<34:
   print("less")
elif x==34:
   print("equal")
else:
   print("greater")

digits = [0, 1, 5,"hello"]

for i in digits:
    print(i)
else:
    print("No items left.")

genre = ['pop', 'rock', 'jazz']

# iterate over the list using index
for i in range(len(genre)):
	print("I like", genre[i])

n=10
sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i+1    # update counter
    print(i)
# print the sum
print("The sum is", sum)


counter = 0

while counter < 3:
    print("Inside loop")
    counter = counter + 1
    print(counter)
else:
    print("Inside else")




# Use of break statement inside loop

for val in "string":
    if val == "i":
        break
    print(val)

print("The end")




# Program to show the use of continue statement inside loops

for val in "string":
    if val == "i":
        continue
    print(val)

print("The end")



# pass is just a placeholder for
# functionality to be added later.
sequence = {'p', 'a', 's', 's'}
for val in sequence:
 #   pass
    print (val)



























