from Core.cpu import get_cpu

CPU = get_cpu()  # The second "cpu" refers to the dictionary defined inside cpu.py

print(CPU)  # Or print(CPU["usage"]) to print only the usage percentage or another key from the dictionary.