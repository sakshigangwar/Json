import json
dict ={"emp1":{
    "name":"lisa",
    "distignation":"progmer",
    "age":"34",
    "salary":"54000"
    },
"emp2":{
    "name":"elis",
    "designation":"trainee",
    "age":"24",
    "salary":"40000"},
    }
out_file = open("file.json","w")
json.dump(dict,out_file,indent=4)
out_file.close()