import pandas as pd
import numpy as np
import json

from os.path import join

last_level = [  {
                "id_list":range(1,2161),
                "cod_list":["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P"],
                "object":[
                            {"cod":"A","des":"U ≤ 0,23 kV"},
                            {"cod":"B","des":"U = 0,4 kV"},
                            {"cod":"C","des":"U = 1 kV"},
                            {"cod":"D","des":"U = 3 kV"},
                            {"cod":"E","des":"U = 5 kV"},
                            {"cod":"F","des":"U = 5,5 kV"},
                            {"cod":"G","des":"U = 6 kV"},
                            {"cod":"H","des":"U = 6,6 kV"},
                            {"cod":"I","des":"U = 10 kV"},
                            {"cod":"J","des":"U = 11 kV"},
                            {"cod":"K","des":"U = 12 kV"},
                            {"cod":"L","des":"U = 13,2 kV"},
                            {"cod":"M","des":"U = 15 kV"},
                            {"cod":"N","des":"U = 16 kV"},
                            {"cod":"O","des":"U = 20 kV"},
                            {"cod":"P","des":"U = 22 kV"},
                            {"cod":"Q","des":"U = 24 kV"},
                            {"cod":"R","des":"U = 25 kV"},
                            {"cod":"S","des":"U = 30 kV"},
                            {"cod":"T","des":"U = 33 kV"}
                            ]
                },
                {
                "id_list":range(1,2161),
                "cod_list":["Q","R","S","T"],
                "object":[
                            {"cod":"U","des":"U = 45 kV"},
                            {"cod":"V","des":"U = 50 kV"},
                            {"cod":"W","des":"U = 55 kV"},
                            {"cod":"X","des":"U = 66 kV"},
                            {"cod":"Y","des":"U = 110 kV"},
                            {"cod":"Z","des":"U = 130 kV"},
                            {"cod":"1","des":"U = 132 kV"},
                            {"cod":"2","des":"U = U = 150 kV"},
                            {"cod":"5","des":"Otros"}
                            ]
                },
                {
                "id_list":range(2161,3016),
                "cod_list":None,
                "object":[
                            {"cod":"0","des":"Posición no utilizada"}
                            ]
                },
                {
                "id_list":range(3016,3106),
                "cod_list":None,
                "object":[
                            {"cod":"A","des":"0 kVA"},
                            {"cod":"B","des":"15 kVA"},
                            {"cod":"C","des":"25 kVA"},
                            {"cod":"D","des":"50 kVA"},
                            {"cod":"E","des":"100 kVA"},
                            {"cod":"F","des":"160 kVA"},
                            {"cod":"G","des":"250 kVA"},
                            {"cod":"H","des":"400 kVA"},
                            {"cod":"I","des":"630 kVA"},
                            {"cod":"J","des":"1000 kVA"},
                            {"cod":"K","des":"1250 kVA"},
                            {"cod":"L","des":"2x15 kVA"},
                            {"cod":"M","des":"2x25 kVA"},
                            {"cod":"N","des":"2x50 kVA"},
                            {"cod":"O","des":"2x100 kVA"},
                            {"cod":"P","des":"2x160 kVA"},
                            {"cod":"Q","des":"2x250 kVA"},
                            {"cod":"R","des":"2x400 kVA"},
                            {"cod":"S","des":"2x630 kVA"},
                            {"cod":"T","des":"2x1000 kVA"},
                            {"cod":"U","des":"2x1250 kVA"},
                            {"cod":"V","des":"Otros no reparto o reflexión"},
                            {"cod":"Z","des":"Centro de reparto o reflexión"}
                            ]
                },
                {
                "id_list":range(3106,3110),
                "cod_list":None,
                "object":[
                            {"cod":"0","des":"Posición no utilizada"}
                            ]
                },
                {
                "id_list":range(3110,3327),
                "cod_list":None,
                "object":[
                            {"cod":"1","des":"Clase A según UNE-EN 61000-4-30"},
                            {"cod":"2","des":"Clase S según UNE-EN 61000-4-30"},
                            {"cod":"3","des":"Clase B según UNE-EN 61000-4-30"},
                            {"cod":"4","des":"Otros (especificar características en nota)"}
                            ]
                },
                {
                "id_list":range(3327,3436),
                "cod_list":None,
                "object":[
                            {"cod":"1","des":"En subestación"},
                            {"cod":"2","des":"En centro de transformación"},
                            {"cod":"3","des":"En tramo de línea"}
                            ]
                },
                {
                "id_list":range(3436,3996),
                "cod_list":None,
                "object":[
                            {"cod":"1","des":"Trafo en servicio"},
                            {"cod":"2","des":"Trafo de reserva"},
                            {"cod":"3","des":"Trafo móvil"}
                            ]
                },
                {
                "id_list":range(3996,4260),
                "cod_list":None,
                "object":[
                            {"cod":"C","des":"U = 1 kV"},
                            {"cod":"D","des":"U = 3 kV"},
                            {"cod":"E","des":"U = 5 kV"},
                            {"cod":"F","des":"U = 5,5 kV"},
                            {"cod":"G","des":"U = 6 kV"},
                            {"cod":"H","des":"U = 6,6 kV"},
                            {"cod":"I","des":"U = 10 kV"},
                            {"cod":"J","des":"U = 11 kV"},
                            {"cod":"K","des":"U = 12 kV"},
                            {"cod":"L","des":"U = 13,2 kV"},
                            {"cod":"M","des":"U = 15 kV"},
                            {"cod":"N","des":"U = 16 kV"},
                            {"cod":"O","des":"U = 20 kV"},
                            {"cod":"P","des":"U = 22 kV"},
                            {"cod":"Q","des":"U = 24 kV"},
                            {"cod":"R","des":"U = 25 kV"},
                            {"cod":"S","des":"U = 30 kV"},
                            {"cod":"T","des":"U = 33 kV"},
                            {"cod":"U","des":"U = 45 kV"},
                            {"cod":"V","des":"U = 50 kV"},
                            {"cod":"W","des":"U = 55 kV"},
                            {"cod":"X","des":"U = 66 kV"},
                            {"cod":"Y","des":"U = 110 kV"},
                            {"cod":"Z","des":"U = 130 kV"},
                            {"cod":"1","des":"U = 132 kV"},
                            {"cod":"2","des":"U = 150 kV"},
                            {"cod":"5","des":"Otros"}
                            ]
                },
                {
                "id_list":range(4260,5557),
                "cod_list":None,
                "object":[
                            {"cod":"0","des":"Posición no utilizada"}
                            ]
                }
                ]

def catch_lastlevel(ID,CODE):
    for dictionary in last_level:
        id_list = dictionary["id_list"]
        cod_list = dictionary["cod_list"]
        if cod_list is None:
            if ID in id_list:
                lastlevel = dictionary["object"]
                return lastlevel
        else:
            if (ID in id_list) and (CODE in cod_list):
                lastlevel = dictionary["object"]
                return lastlevel
    print("some problems")



instance1 = pd.read_csv(join("BUILDER","CINI_config","CINI_2 - PRIMERA.csv")).values

instance2 = pd.read_csv(join("BUILDER","CINI_config","CINI_2 - SEGUNDA.csv")).values

instance3 = pd.read_csv(join("BUILDER","CINI_config","CINI_2 - TERCERA.csv")).values

instance4 = pd.read_csv(join("BUILDER","CINI_config","CINI_2 - CUARTA.csv")).values

instance5 = pd.read_csv(join("BUILDER","CINI_config","CINI_2 - QUINTA.csv")).values

instance6 = pd.read_csv(join("BUILDER","CINI_config","CINI_2 - SEXTA.csv")).values

#instance7 = pd.read_csv("BUILDER\CINI_config\CINI - SEPTIMA.csv").values


index_1 , index_2, index_3 ,index_4 , index_5 , index_6, index_7= 0, 0, 0,0, 0, 0, 0
CINI = {"cini":[]}
while len(instance1)>0:
    instance_row1 = instance1[0]
    unique1, cod1, des1 = instance_row1
    level_1 = {"cod":cod1,"des":des1, "next":[]}
    CINI["cini"].append(level_1)
    
    count_2 = 0
    while len(instance2)>0 and count_2 < 100:
        count_2 +=1
        instance_row2 = instance2[0]
        unique_2, link2, cod2, des2 = instance_row2
        if str(unique1) == str(link2):
            level_2 = {"cod":cod2, "des":des2, "next":[]}
            CINI["cini"][index_1]["next"].append(level_2)

            count_3 = 0
            while len(instance3)>0 and count_3 <300:
                count_3 +=1
                instance_row3 = instance3[0]
                unique_3, link3, cod3, des3 = instance_row3
                if str(unique_2) == str(link3):
                    level_3 = {"cod":cod3, "des":des3, "next":[]}
                    CINI["cini"][index_1]["next"][index_2]["next"].append(level_3)

                    count_4 = 0
                    while len(instance4)>0 and count_4 <  500:
                        count_4 +=1
                        instance_row4 = instance4[0]
                        unique_4, link4, cod4, des4 = instance_row4
                        if str(unique_3) == str(link4):
                            level_4 = {"cod":cod4, "des":des4, "next":[]}
                            CINI["cini"][index_1]["next"][index_2]["next"][index_3]["next"].append(level_4)

                            count_5 = 0
                            while len(instance5)>0 and count_5 <  800:
                                count_5 +=1
                                instance_row5 = instance5[0]
                                unique_5, link5, cod5, des5 = instance_row5
                                if str(unique_4) == str(link5):
                                    level_5 = {"cod":cod5, "des":des5, "next":[]}
                                    CINI["cini"][index_1]["next"][index_2]["next"][index_3]["next"][index_4]["next"].append(level_5)

                                    count_6 = 0
                                    while len(instance6)>0 and count_6 < 8000:
                                        count_6 +=1
                                        instance_row6 = instance6[0]
                                        unique_6, link6, cod6, des6 = instance_row6
                                        if str(unique_5) == str(link6) :
                                            seventh_level = catch_lastlevel(unique_6,cod6)
                                            level_6 = {"cod":cod6, "des":des6, "next":seventh_level}
                                            CINI["cini"][index_1]["next"][index_2]["next"][index_3]["next"][index_4]["next"][index_5]["next"].append(level_6)
                                            
                                            print(len(instance6))
                                            index_6 +=1
                                            instance6 = np.delete(instance6, 0, 0)

                                    index_6 = 0
                                    index_5 +=1
                                    instance5 = np.delete(instance5, 0, 0)
                            
                            index_5 = 0
                            index_4 +=1
                            instance4 = np.delete(instance4, 0, 0)                   
                    index_4 = 0
                    index_3 +=1
                    instance3 = np.delete(instance3, 0, 0)
            index_3 = 0
            index_2 +=1
            instance2 = np.delete(instance2, 0, 0)
    index_2 =0   
    index_1 += 1
    instance1 = np.delete(instance1, 0, 0)

CINI_STRING = json.dumps(CINI,indent=4)

file1 = open(join("cini","CONFIG_FILE","CINI_Configuration_File_1.json"),"w+") 
file1.write(CINI_STRING)
file1.close()

print("finish building CINI_Configuration_File")
