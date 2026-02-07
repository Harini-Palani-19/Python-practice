marks=[]
while True:
  print("\n1.Add Marks")
  print("2.Show Marks")
  print("3.Average")
  print("4.Highest & Lowest")
  print("5.Exit")

choice=int(input("Enter choice: ")) 

if choice==1:
   m=int(input("Enter mark:"))
   marks.append(m)
elif choice==2:
  print("Marks:",marks)
elif choice==3:
   if marks:
     print("Average=",sum(marks)/len(marks))
   else:
     print("No data") 
elif choice==4:
  if marks:
    print("Highest=",max(marks))
    print("Lowest=",min(marks))
  else:
    print("No data")
elif choice==5:
  break     
else:
  print("Invalid choice")
  
