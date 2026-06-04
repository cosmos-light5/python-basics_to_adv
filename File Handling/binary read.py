#
with open("Scr.png", "rb") as f: 
    binary_data=f.read()
    print(f"Read {len(binary_data)} bytes")


with open("Jorosan.png", "wb") as f:            
    f.write(binary_data)