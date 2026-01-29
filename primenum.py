startnum=int(input("Enter a number:"))
endnum=int(input("Enter a number:"))
for num in range(startnum,endnum+1):
  if num>1:
    for i in range(2,num):
      if num%i==0:
        break
      else:
        print(num)
        
