import pandas as pd
import numpy as np

import json




instance1 = pd.read_csv("CINI_config\CINI - PRIMERA.csv").values

instance2 = pd.read_csv("CINI_config\CINI - SEGUNDA.csv").values

instance3 = pd.read_csv("CINI_config\CINI - TERCERA.csv").values

instance4 = pd.read_csv("CINI_config\CINI - CUARTA.csv").values

instance5 = pd.read_csv("CINI_config\CINI - QUINTA.csv").values

instance6 = pd.read_csv("CINI_config\CINI - SEXTA.csv").values

instance7 = pd.read_csv("CINI_config\CINI - SEPTIMA.csv").values


index_1 , index_2, index_3 ,index_4 , index_5 , index_6, index_7= 0, 0, 0,0, 0, 0, 0
CINI = {"cini":[]}
while len(instance1)>0:
    instance_row1 = instance1[0]
    cod1, des1 = instance_row1
    level_1 = {"cod":cod1,"des":des1, "next":[]}
    CINI["cini"].append(level_1)
    count_2 = 0
    while len(instance2)>0 and count_2 < 3* len(instance2)+1:
        count_2 +=1
        instance_row2 = instance2[0]
        link2, cod2, des2 = instance_row2
        if str(cod1) == str(link2):
            level_2 = {"cod":cod2, "des":des2, "next":[]}
            CINI["cini"][index_1]["next"].append(level_2)
        
            count_3 = 0
            while len(instance3)>0 and count_3 < 3* len(instance3)+1:
                count_3 +=1
                instance_row3 = instance3[0]
                link3, cod3, des3 = instance_row3
                if str(cod2) == str(link3) and str(cod1) == str(link2):
                    level_3 = {"cod":cod3, "des":des3, "next":[]}
                    CINI["cini"][index_1]["next"][index_2]["next"].append(level_3)

                    count_4 = 0
                    while len(instance4)>0 and count_4 <  3*len(instance4)+1:
                        if (index_1 == 1):
                            print("ggg")
                        count_4 +=1
                        instance_row4 = instance4[0]
                        link4, cod4, des4 = instance_row4
                        if str(cod3) == str(link4) and str(cod2) == str(link3) and str(cod1) == str(link2):
                            level_4 = {"cod":cod4, "des":des4, "next":[]}
                            if des4 == "Propiedad empresa distribuidora":
                                print("fff")
                            CINI["cini"][index_1]["next"][index_2]["next"][index_3]["next"].append(level_4)

                            count_5 = 0
                            while len(instance5)>0 and count_5 <  4*len(instance5)+1:
                                count_5 +=1
                                instance_row5 = instance5[0]
                                link5, cod5, des5 = instance_row5
                                if str(cod4) == str(link5) and str(cod3) == str(link4) and str(cod2) == str(link3) and str(cod1) == str(link2):
                                    level_5 = {"cod":cod5, "des":des5, "next":[]}
                                    CINI["cini"][index_1]["next"][index_2]["next"][index_3]["next"][index_4]["next"].append(level_5)

                                    count_6 = 0
                                    while len(instance6)>0 and count_6 < 5*len(instance6)+1:
                                        count_6 +=1
                                        instance_row6 = instance6[0]
                                        link6, cod6, des6 = instance_row6
                                        if str(cod5) == str(link6) and str(cod4) == str(link5) and str(cod3) == str(link4) and str(cod2) == str(link3) and str(cod1) == str(link2):
                                            level_6 = {"cod":cod6, "des":des6, "next":[]}
                                            CINI["cini"][index_1]["next"][index_2]["next"][index_3]["next"][index_4]["next"][index_5]["next"].append(level_6)

                                            count_7 = 0
                                            while len(instance7)>0 and count_7 < 10*len(instance7)+1:
                                                count_7 +=1
                                                instance_row7 = instance7[0]
                                                link7, cod7, des7 = instance_row7
                                                if str(cod6) == str(link7) and str(cod5) == str(link6) and str(cod4) == str(link5) and str(cod3) == str(link4) and str(cod2) == str(link3) and str(cod1) == str(link2):
                                                    level_7 = {"cod":cod7, "des":des7,"next":[]}
                                                    CINI["cini"][index_1]["next"][index_2]["next"][index_3]["next"][index_4]["next"][index_5]["next"][index_6]["next"].append(level_7)
                                                    #index_7 +=1
                                                    instance7 = np.delete(instance7, 0, 0) 
                                                    print(count_7,len(instance7))
                                            #index_7 = 0
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

file1 = open("CINI_JSON1.json","w+") 
file1.write(CINI_STRING)
file1.close()


