c1={"idly":150,"dosa":180,"biryani":200,"parotta":100}
n = int(input("How many products do you want? "))
total = 0
for i in range(n):
    item = input("Enter order name: ")
    qty = int(input("Enter quantity: "))
    total +=c1[item]*qty
print("total price=",total)
 