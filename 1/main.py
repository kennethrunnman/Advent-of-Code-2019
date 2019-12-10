def read_file():
    f = open("input.txt","r")
    f1 = f.readlines()
    return f1

def get_fuel(mass):
    rest = mass % 3
    mass = mass - rest
    fuel = (mass / 3) - 2
    return fuel

def calc_fuel_req(f1):
    sum = 0
    for mass in f1:
        fuel = get_fuel(float(mass))
        sum += fuel
    sum = int(sum)
    return sum

def calc_all_fuel(f1):
    sum = 0
    for mass in f1:
        x = float(mass)
        while(x >= 3.0):
            x = get_fuel(x)
            if(x > 0):
                sum += x
    sum = int(sum)
    return sum


def main():
    f1 = read_file()
    sum = calc_fuel_req(f1)
    print(sum) # part 1
    sum2 = calc_all_fuel(f1)
    print(sum2) # part 2



main()
