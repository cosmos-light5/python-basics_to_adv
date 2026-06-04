import json

data={'name': 'John', 'age': '30', 'city':'New York'}
with open ('output.json','w') as file:
    json.dump(data,file)

with open ('pretty_output.jason','w') as file:
    json.dump(data, file, indent=4)

with open ('pretty_output.jason','w') as file:
    json.dump(data, file, 
              indent=4,                     
              sort_keys=True,               
              ensure_ascii=False)
    



with open('output.json', 'r') as file:
    data= json.load(file)
 
