#Reading a binary file (like an image)
with open("Scr.png", "rb") as f: 
    binary_data=f.read()
    print(f"Read {len(binary_data)} bytes")


# wirting binary data
with open("Scr-copy.png", "wb") as f: 
    f.write(binary_data)


""" with open("Jorosan.png", "wb") as f:            
    f.write(binary_data) """