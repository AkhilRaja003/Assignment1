a = int(input("enter 1st position number:"))
b = int(input("enter 1st position number:"))

list = ["Akhil","Sunny","Abhi","Sisi","Naveen","Navya","Rakesh","Rahul","Nani"]

list[a],list[b] = list[b],list[a]

print(list)

print("**********************************************")
