# import logging
# #comfigure logging
# logging.basicConfig(
#     level=logging.DEBUG,
#     format="%(asctime)s - %(levelname)s - %(message)s",
#     filename="app.log" 
# )

# def divide_numbers(a,b):
#     logging.debug(f"Dividing {a} by {b}")
#     try:
#         result=a/b
#         logging.info(f"Division result: {result}")
#         return result
#     except ZeroDivisionError:
#         logging.error("Division by zero attempted")
#         raise

# try:
#     divide_numbers(10,5)
# except ZeroDivisionError:
#     print("Cannot divide by zero..")


import pdb
def complex_function(a,b):
    result=a*b
    pdb.set_trace()         #production level ma use na garne
    c=20
    if result>50:
        pdb.set_trace()     #
        return "Large result"
    return "small result"

complex_function(10,7)