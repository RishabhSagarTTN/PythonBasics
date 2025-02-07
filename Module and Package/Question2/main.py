from importlib import reload
import pkg.mod
import pkg 

pkg.hi()# using method hi directly from the mod without doing pkg.mod.hi() beacuse we import
#it in the __init__ 
while True:
    reload(pkg.mod)# remember to put module name in the reload and if in the package
    #import the module and use generic way dont use from way
    pkg.mod.hello()
    input("Enter")

