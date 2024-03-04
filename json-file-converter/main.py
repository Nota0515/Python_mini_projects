import json


if __name__=='__main__':
  try:
    with open('input.json','r') as f:
        data = json.loads(f.read())

        obj = ','.join([*data[0]])

        for objs in data:
            obj += f'\n{objs["Name"]},{objs["STD"]},{objs["Gender"]}'
        
        with open('output.csv','w') as f:
            f.write(obj)
  except Exception as ex:
    print(f"ERROR 404: {str(ex)}")

  
  