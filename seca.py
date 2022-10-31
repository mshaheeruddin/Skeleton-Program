x = int(input("Enter an integer greater than 1: "))
Product = 1
Factor = 0
while Product < x:
    Factor = Factor + 1 
    Product = Product * Factor
if x == Product:
    Product = 1    
    for n in range(1,Factor + 1):
      Product = Product * n 
      print(n)
else: 
    print('No Result')


   

