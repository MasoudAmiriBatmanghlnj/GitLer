print("_____________Strat_____________")

hex_data= input("Enter Hex: ")

length= len(hex_data)

print(f"input: {hex_data} ")


valid = all(c in "123456789abcdefABCDEF" for c in hex_data)

print(f"length: {length} ")

if not valid:
    
    print("Invalid Hex characters")

elif length == 0:
    print("Empty input")

elif length %2 !=0:
    print("Odd number of digits")

else:
    print("Valid Hex input")

print("___________________End_________________")



