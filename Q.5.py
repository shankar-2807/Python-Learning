#A man goes for shopping. He buys 5 products. Accept the price of all products and display the total bill after adding 18% GST.

pro1 = int(input("Enter 1st product price: "))
pro2 = int(input("Enter 2nd product price: "))
pro3 = int(input("Enter 3rd product price: "))
pro4 = int(input("Enter 4th product price: "))
pro5 = int(input("Enter 5th product price: "))

bill = (pro1 + pro2 + pro3 + pro4 + pro5)
GST_Bill =(bill + bill * 18 / 100) 
print("Total_Bill: ", GST_Bill)

