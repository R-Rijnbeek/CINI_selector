import sys
sys.path.append('.')

from src.cini_selector import CINI_Constructor

pr = CINI_Constructor()

pr.Define_Selector(["3","1","0","2","3","T","0"])
#pr.Define_Selector(["2","0","2","1"])
print(pr.Selector_CINI_getter())
print(pr.CINI_Builder())
print(pr.Is_CINI_Complete())
print(pr.CINI_getter())
pr.CINI_reset()
print(pr.CINI_getter())