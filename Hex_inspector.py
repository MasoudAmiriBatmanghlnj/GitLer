print("_____________________________________________________________")

hex_data= input("Enter Hex: ")

length= len(hex_data)

print(f"input: {hex_data} ")


valid = all(c in "123456789abcdefABCDEF" for c in hex_data)


if not valid:
    
    print("Invalid Hex characters")

elif length == 0:
    print("Empty input")

elif length %2 !=0:
    print("Odd number of digits")

else:
    data = bytes.fromhex(hex_data)

    print(f"Length: {length}")
    print(f"Bytes: {len(data)}")

    result = " ".join(f"{d:02X}" for d in data)

    print(f"Hex: {result}")
    
print("__________________________________________________________")



