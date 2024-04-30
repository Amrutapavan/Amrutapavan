import example_module as mod
import platform

x = platform.system()
print(x)

mod.greeting("AmruthaPavan")
Data = mod.person_details["age"]
print(Data)
print(dir(mod))