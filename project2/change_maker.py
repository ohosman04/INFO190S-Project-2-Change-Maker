nickels = 25
dimes = 25
quarters = 25
ones = 0
fives = 0
i = 1

print("Welcome to the vending machine change maker program")
print("Change maker initialized.")
print("Stock contains:")    
print(f"   {nickels} nickels")
print(f"   {dimes} dimes")    
print(f"   {quarters} quarters")
print(f"   {ones} ones")
print(f"   {fives} fives")
print()
while i > 0:
    nickelback = 0
    dimeback = 0
    quarterback = 0
    oneback = 0
    fiveback = 0
    
    purchase_price = input("Enter the purchase price (xx.xx) or `q' to quit: ")
    if "." in purchase_price:
        dollars,cents = purchase_price.split(".")
    elif purchase_price.isdigit():
        dollars = purchase_price
        cents = "0"
    else:
        dollars = "big chungus"
        cents = "nickelback"
    if cents == "":
        cents = "0"
    elif dollars == "":
        dollars = "0"
    
    if purchase_price == "q":
        i = 0
    elif purchase_price != "q":
        if (dollars.isdigit() == False) or (cents.isdigit() == False):
            print("Invalid purchase amount. Try again")
        elif (float(purchase_price) * 100) % 5 != 0 or (float(purchase_price) * 100) < 0:
            print("Illegal price: Must be a non-negative multiple of 5 cents. \n")
        else:
            print("Menu for purchase:")
            print("  'n' - deposit a nickel")
            print("  'd' - deposit a dime")
            print("  'q' - deposit a quarter")
            print("  'o' - deposit a one dollar bill")
            print("  'f' - deposit a five dollar bill")
            print("  'c' - cancel the purchase")
            print()
            total = int((float(dollars) + (float(cents) / 100))*100)
            deposit_amount = 0
            
            while deposit_amount < (float(purchase_price) * 100):
                deposit = input("Indicate your deposit: ").lower()
                if deposit == "o":
                    #print(f"Payment due: {int((total) // 100)- 1} dollars and {int(((total) % 100) - 0)} cents")
                    total -= 100
                    ones += 1
                    deposit_amount += 100
                elif deposit == "f":
                    #print(f"Payment due: {int((total) // 100)- 5} dollars and {int(((total) % 100) - 0)} cents")
                    total -= 500
                    fives +=1
                    deposit_amount += 500
                elif deposit =="n":
                    #print(f"Payment due: {int((total) // 100)- 0} dollars and {int(((total) % 100) - 5)} cents")
                    total -= 5
                    nickels += 1
                    deposit_amount += 5  
                elif deposit == "d":
                    #print(f"Payment due: {int((total) // 100)- 0} dollars and {int(((total) % 100) - 10)} cents")
                    total -= 10
                    dimes += 1
                    deposit_amount += 10 
                elif deposit =='q':
                    #print(f"Payment due: {int((total) // 100)- 0} dollars and {int(((total) % 100) - 25)} cents")
                    total -= 25
                    quarters += 1
                    deposit_amount += 25     
                elif deposit == 'c':
                    break
                else:
                    print(f"Illegal Selection: {deposit}")
                if deposit_amount < (float(purchase_price) * 100):
                    print(f"Payment due: {int((total) // 100)} dollars and {int(((total) % 100))} cents")
            if total <= 0:
                change = int(-total)
            else:
                change = int(deposit_amount)
            
            if change > 0:
                print("\nPlease take the change below.")
            else:
                print("\nPlease take the change below.")
                print("  No change due.")

             #fiveback += min(change // 500,fives)
             #change-= fiveback * 500
             #fives -= fiveback
             #oneback += min(change // 100,ones)
             #change-= oneback * 100
             #ones -= oneback
            quarterback += min(change // 25,quarters)
            change-= quarterback * 25
            quarters -= quarterback
            dimeback += min(change // 10,dimes)
            dimes -= dimeback
            change-= dimeback * 10
            nickelback += min(change // 5,nickels)
            change-= nickelback * 5
            nickels -= nickelback
            if fiveback > 0:
                print(f"   {fiveback} fives")
            if oneback > 0:
                print(f"   {oneback} ones")
            if quarterback > 0:
                print(f"   {quarterback} quarters")
            if dimeback > 0:
                print(f"   {dimeback} dimes")
            if nickelback > 0:
                print(f"   {nickelback} nickels")   
            if change > 0:
                print("Machine is out of change.")
                print("See store manager for remaining refund.")
                if change >= 100:
                    print(f"Amount due is: {int((change) // 100)} dollars and {int(((change) % 100))} cents")
                elif change % 100 == 0:
                    print(f"Amount due is: {int((change) // 100)} dollars")
                else:
                    print(f"Amount due is: {int(((change) % 100))} cents")

            print("\nStock contains: ")    
            print(f"   {nickels} nickels")
            print(f"   {dimes} dimes")    
            print(f"   {quarters} quarters")
            print(f"   {ones} ones")
            print(f"   {fives} fives")
            print()
