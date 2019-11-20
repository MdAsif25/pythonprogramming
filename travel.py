
name=input("enter your name:")
age=input("enter your age:")
phone=input("enter your phone number:")
mail=input("enter your mail:")
run=True
while run:
  run=False
  source=input("source:")
  destination=input("destination:")
  if(source==destination):
      print("don't select the same location")
      run=True
      continue
if(source=="salem"):
    source=int(0)
if(source=="pachal"):
    source=int(25)
if(source=="namkkal"):
    source=int(50)
if(destination=="salem"):
    destination=int(0)
if(destination=="pachal"):
    destination=int(25)
if(destination=="namkkal"):
    destination=int(50)
dist=destination-source
print(dist)
vehicles=["car","bus"]
print(vehicles)
veh=input("vehicles:")
customer=["premium","ordinary"]
print(customer)
cust=input("cutomertype:")
if(cust=="premium"):
    amt=7*dist
    print("amount is ",amt)
else:
    amt=12*dist
    print("amount is",amt)
