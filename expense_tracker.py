condition=True
expense={}
total=0
parts=[]
remaining_tasks={}
f=open("expense_tracker.txt","r")
c=f.readlines()
for i in c:
    parts=i.split(",")
    expense[parts[0]]=int(parts[1])
def add_expense():
    n1=input("enter expense name:")
    n2=int(input("enter expense:"))
    if n1 in expense:
        n2 = expense[n1] + n2 #expense[n1]=to get the value of n1
        expense[n1] = n2 #updating the new value to the key n1
    else:
        expense[n1]=n2
    m=open("expense_tracker.txt","w")
    for i,h in expense.items():
        m.write(i+","+ str(h) + "\n")
    m.close()
def view_expense():
    m=open("expense_tracker.txt","r")
    c=m.readlines()
    for i in c:
        print(i.strip())
def delete_expense():
    n3=input("enter the expense name you want to delete:")
    for i,h in expense.items():
        if i!=n3:
            remaining_tasks[i]=h
    for l,m in remaining_tasks.items():
        t=open("expense_tracker.txt","w")
        t.write(l+ "," + str(m) + "\n")
        t.close()
def view_total():
    total=sum(expense.values())
    print(total)
while condition:
    print("_________EXPENSE TRACKER CLI_________")
    print("1:add expense:")
    print("2:view expense:")
    print("3:view total")
    print("4:delete expense:")
    print("5:exit")
    try:
        choice=int(input("enter your choice"))
    except ValueError:
        print("invalid input")
    if choice==1:
        add_expense()
    elif choice==2:
        view_expense()
    elif choice==3:
        view_total()
    elif choice==4:
        delete_expense()
    elif choice==5:
        condition=False
    else:
        print("invalid choice")
    