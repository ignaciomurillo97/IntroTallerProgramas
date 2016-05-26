cateto1 = input("cateto: ")
cateto2 = input("otro cateto: ")



if (cateto1.isnumeric() and cateto2.isnumeric()):
  cateto1 = int(cateto1)
  cateto2 = int(cateto2)  

if (cateto1 > 0 and cateto2 > 0):
  area = cateto1 * cateto2 / 2
  print("area: ", area)
  
