#Exercise 8:Widgets and Gizmos
#(15 Lines)
#An online retailer sells two products: widgets and gizmos. Each widget weighs 75
#grams. Each gizmo weighs 112 grams. Write a program that reads the number of
#widgets and the number of gizmos in an order from the user. Then your program
#should compute and display the total weight of the order.


#weights
widget = 75
gizmo = 112

def weight_calc():
    num_widget = int(input("How many widgets would you like to buy? "))
    num_gizmo = int(input("How many gizmos would you like to buy? "))
    total_weight = (num_widget * widget) + (num_gizmo * gizmo)
    return str(total_weight) + " grams"

print(weight_calc())
