

def read_file():
    f = open("input.txt","r")
    contents = f.read()
    return contents

def run_program(intcode):
    for i in range(0, len(intcode), 4):
        opcode = intcode[i]
        first_position = int(intcode[i+1])
        second_position = int(intcode[i+2])
        output_position = int(intcode[i+3])
        first_value = int(intcode[first_position])
        second_value = int(intcode[second_position])
        result = 0
        if opcode == "1":
            result = first_value + second_value
        elif opcode == "2":
            result = first_value * second_value
        elif opcode == "99":
            break
        else:
            print("Something is Wrong")
            break
        intcode[output_position] = str(result)
    return intcode

def main():
    message = read_file()
    # Part I
    intcode = message.split(",")
    intcode[1] = "12"
    intcode[2] = "2"
    new_intcode = run_program(intcode)
    print(new_intcode[0])
    # Part II
    for verb in range(0, 99):
        for noun in range(0, 99):
            intcode2 = message.split(",")
            intcode2[1] = verb
            intcode2[2] = noun
            new_intcode2 = run_program(intcode2)
            if(new_intcode2[0] == "19690720"):
                print(verb, noun)

main()
