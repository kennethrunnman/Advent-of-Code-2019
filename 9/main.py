def read_file():
    f = open("in.txt","r")
    contents = f.read()
    return contents

def run_program(intcode):
    i = 0
    stop = False
    last_output = 0
    inputs = []
    #inputs.append(str(input2))
    #inputs.append(str(input))
    relative_base = 0
    #print(inputs)
    while(not stop):
        print(i, len(intcode), intcode[i])
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
        if opcode == "1" or opcode == "2" or opcode == "5" or opcode == "6" or opcode == "7" or opcode == "8":
            first_value = -1
            second_value = -1
            if(mode1 == 0):
                first_position = int(intcode[i+1])
                print(first_position)
                first_value = int(intcode[first_position])
            elif(mode1 == 1):
                first_value = int(intcode[i+1])
            elif(mode1 == 2):
                first_position = relative_base + int(intcode[i+1])
                first_value = int(intcode[first_position])
            if(mode2 == 0):
                second_position = int(intcode[i+2])
                second_value = int(intcode[second_position])
            elif(mode2 == 1):
                second_value = int(intcode[i+2])
            elif(mode1 == 2):
                first_position = relative_base + int(intcode[i+1])
                first_value = int(intcode[first_position])
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
        elif(opcode == "9"):
            first_value = 0
            first_position = 0
            if(mode1 == 0):
                first_position = int(intcode[i+1])
                first_value = int(intcode[first_position])
            elif(mode1 == 1):
                first_value = int(intcode[i+1])
            elif(mode1 == 2):
                first_position = relative_base + int(intcode[i+1])
                first_value = int(intcode[first_position])
            relative_base = first_value
            i += 2
        elif opcode == "3":
            output_position = int(intcode[i+1])
            result = inputs.pop()
            intcode[output_position] = str(result)
            i += 2
            print("IN", str(result))
        elif opcode == "4":
            output_value = -1
            if(mode1 == 0):
                output_position = int(intcode[i+1])
                output_value = int(intcode[output_position])
                i += 2
                print("OUT", output_value)
                #return output_value, 0, i
            elif(mode1 == 1):
                output_value = int(intcode[i+1])
                i += 2
                print("OUT", output_value)
                #return output_value, 0, i
            elif(mode1 == 2):
                first_position = relative_base + int(intcode[i+1])
                first_value = int(intcode[first_position])
                i += 2
                print("OUT", output_value)
            #last_output = output_value,
        elif int(instruction) == "99":
            print("STOP", input)
            stop = True
            #return input, 1, i
        else:
            print("Something is Wrong")
            stop = True
    return last_output

def main():
    contents = read_file()
    intcode = contents.split(",")
    for i in range(0, 100000):
        intcode.append("0")
    run_program(intcode)

main()
