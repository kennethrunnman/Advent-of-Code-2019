def read_file():
    f = open("input.txt","r")
    contents = f.read()
    return contents

def run_program(intcode):
    i = 0
    input = 1
    stop = False
    while(not stop):
        instruction = intcode[i]
        last = len(instruction) - 1
        opcode = instruction[last]
        mode1 = 0
        mode2 = 0
        if(last >= 2):
            mode1 = int(instruction[last-2])
        if(last >= 3):
            mode2 = int(instruction[last-3])
        result = 0
        #print(i, intcode[i], intcode[i+1], intcode[i+2], intcode[i+3], opcode, mode1, mode2)
        if opcode == "1" or opcode == "2":
            first_value = -1
            second_value = -1
            #print(mode1)
            if(mode1 == 0):
                first_position = int(intcode[i+1])
                first_value = int(intcode[first_position])
                #print("hej")
            else:
                first_value = int(intcode[i+1])
            if(mode2 == 0):
                second_position = int(intcode[i+2])
                second_value = int(intcode[second_position])
            else:
                second_value = int(intcode[i+2])
            if(opcode == "1"):
                result = first_value + second_value
            else:
                result = first_value * second_value
            output_position = int(intcode[i+3])
            intcode[output_position] = str(result)
            #print("first", first_value, "second", second_value)
            i += 4
        elif opcode == "3":
            output_position = int(intcode[i+1])
            result = input
            intcode[output_position] = str(result)
            i += 2
        elif opcode == "4":
            output_value = -1
            if(mode1 == 0):
                output_position = int(intcode[i+1])
                output_value = int(intcode[output_position])
            else:
                output_value = int(intcode[i+1])
            print("Output", output_value)
            i += 2
        elif instruction == "99":
            stop = True
        else:
            print("Something is Wrong")
            stop = True
    return intcode

def run_program2(intcode):
    i = 0
    input = 5
    stop = False
    while(not stop):
        instruction = intcode[i]
        last = len(instruction) - 1
        opcode = instruction[last]
        mode1 = 0
        mode2 = 0
        if(last >= 2):
            mode1 = int(instruction[last-2])
        if(last >= 3):
            mode2 = int(instruction[last-3])
        result = 0
        #print(i, intcode[i], intcode[i+1], intcode[i+2], intcode[i+3], opcode, mode1, mode2)
        if opcode == "1" or opcode == "2" or opcode == "5" or opcode == "6" or opcode == "7" or opcode == "8":
            first_value = -1
            second_value = -1
            #print(mode1)
            if(mode1 == 0):
                first_position = int(intcode[i+1])
                first_value = int(intcode[first_position])
                #print("hej"
            else:
                first_value = int(intcode[i+1])
            if(mode2 == 0):
                second_position = int(intcode[i+2])
                second_value = int(intcode[second_position])
            else:
                second_value = int(intcode[i+2])
            if(opcode == "1"):
                result = first_value + second_value
                output_position = int(intcode[i+3])
                intcode[output_position] = str(result)
                i += 4
            elif(opcode == "2"):
                result = first_value * second_value
                output_position = int(intcode[i+3])
                intcode[output_position] = str(result)
                i += 4
            elif(opcode == "5"):
                if(not first_value == 0):
                    i = second_value
                else:
                    i += 3
            elif(opcode == "6"):
                if(first_value == 0):
                    i = second_value
                else:
                    i += 3
            elif(opcode == "7"):
                if(first_value < second_value):
                    result = 1
                else:
                    result = 0
                output_position = int(intcode[i+3])
                intcode[output_position] = str(result)
                i += 4
            elif(opcode == "8"):
                if(first_value == second_value):
                    result = 1
                else:
                    result = 0
                output_position = int(intcode[i+3])
                intcode[output_position] = str(result)
                i += 4
            #print("first", first_value, "second", second_value)
        elif opcode == "3":
            output_position = int(intcode[i+1])
            result = input
            intcode[output_position] = str(result)
            i += 2
        elif opcode == "4":
            output_value = -1
            if(mode1 == 0):
                output_position = int(intcode[i+1])
                output_value = int(intcode[output_position])
            else:
                output_value = int(intcode[i+1])
            print("Output", output_value)
            i += 2
        elif instruction == "99":
            stop = True
        else:
            print("Something is Wrong")
            stop = True
    return intcode

def main():
    message = read_file()
    # Part I
    intcode = message.split(",")
    new_intcode = run_program(intcode)
    intcode = message.split(",")
    new_intcode = run_program2(intcode)
    #print(new_intcode[0])

main()
