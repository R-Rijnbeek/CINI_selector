import json

import pandas as pd

csv_dataframe = pd.read_csv("work\ShopWindow - Italian translation  - Dashboard.csv").values

translate_dict =  {}
for row in csv_dataframe:
    head = row[0]
    translate = row[1]
    translate_dict[head]=translate

json_string = json.dumps(translate_dict,indent=0,ensure_ascii=True)

file1 = open("translate.json","w+") 
file1.write(json_string)
file1.close()


