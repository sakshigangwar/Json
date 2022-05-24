import json


d={
    "shopping_list":{ 
        "chaco":"15",
        "Biscuits":"50",
        "Diary_milk":"30",
        "ice_cream":"20",
         } 
}
with open("text.json_list","w") as fh:
    json.dump(d,fh,indent=4)

item1=input("kon sa item kharidna chahate ho")
quant=int(input("tum kitne item kharidne chahate ho"))
with open("text.json_list") as file:
    data=json.load(file)
    for x,y in data.items():
        if item1 in y:
            for a,b in y.items():
                if item1==a:
                    if quant<=int(b):
                        b1=int(b)-quant
                        y[a]=b1
                else:
                    d=quant
                    y[a]=d
        else:
            y[item1]=str(quant)
            print(data)
with open("text.json_list","w") as fh:
    json.dump(data,fh,indent=4)
    