f = open("input.txt", "r")
input = f.read()
modules_masses = input.split('\n')
modules_masses = set(map(lambda x:int(x),modules_masses))

fuel_sum = 0
for module_mass in modules_masses:
    # int() will round down the result
    fuel_sum += int(module_mass/3)-2

print(fuel_sum)
