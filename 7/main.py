def read_file():
    f = open("input.txt","r")
    contents = f.read()
    return contents

def run_program(intcode, input, i, input2):
    stop = False
    last_output = 0
    inputs = []
    inputs.append(str(input2))
    inputs.append(str(input))
    #print(inputs)
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
        if opcode == "1" or opcode == "2" or opcode == "5" or opcode == "6" or opcode == "7" or opcode == "8":
            first_value = -1
            second_value = -1
            if(mode1 == 0):
                first_position = int(intcode[i+1])
                first_value = int(intcode[first_position])
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
                return output_value, 0, i
            else:
                output_value = int(intcode[i+1])
                i += 2
                print("OUT", output_value)
                return output_value, 0, i
            #last_output = output_value,
        elif instruction == "99":
            print("STOP", input)
            stop = True
            return input, 1, i
        else:
            print("Something is Wrong")
            stop = True
    return last_output

def acs(intcode_array, phase_settings):
    max_input = 0
    best_phase = []
    for i in range(0, len(phase_settings)):
        input = 0
        for j in range(0, 5):
            input = run_program(intcode_array[i], phase_settings[i][j], input, 0)
        if input > max_input:
            max_input = input
            best_phase = phase_settings[i]
    #print(max_input, best_phase)print("----------------------------")

def acs2(intcode_array, phase_settings2):
    input = 0
    max_input = 0
    best_phase = []
    for i in range(0, len(phase_settings2)):
        input = 0
        position = 0
        stop = False
        print("----------------------------")
        print("START")
        print("----------------------------")
        position = [0, 0, 0, 0, 0]
        for j in range(0, 5):
            input, stop_value, pos = run_program(intcode_array[i][j], phase_settings2[i][j], position[j], input)
            print("IN", input, "PHASE_SETTINGS", phase_settings2[i], "PHASE", j, "POSITION", position)
            position[j] = pos
        while(not stop):
            for j in range(0, 5):
                input, stop_value, pos = run_program(intcode_array[i][j], input, position[j], 0)
                print("IN", input, "PHASE_SETTINGS", phase_settings2[i], "PHASE", j, "POSITION", position)
                if(stop_value == 1):
                    stop = True
                if input > max_input:
                    max_input = input
                    best_phase = phase_settings2[i]
                position[j] = pos
    print(max_input, best_phase)

def main():
    contents = read_file()
    intcode = contents.split(",")
    intcode_array = []
    for i in range(0, 5):
        intcode_array.append(0)
        intcode_array[i] = []
        for j in intcode:
            intcode_array[i].append(j.strip())
    phase_settings = []
    for i in range(0, 5):
        for j in range(0, 5):
            if(i == j):
                continue
            for k in range(0, 5):
                if(j == k or i == k):
                    continue
                for l in range(0, 5):
                    if(l == k or l == j or l == i):
                        continue
                    for m in range(0, 5):
                        if(m == l or m == k or m == j or m == i):
                            continue
                        else:
                            phase_settings.append([i, j, k, l, m])
    phase_settings2 = []
    for i in range(5, 10):
        #print(i)
        for j in range(5, 10):
            if(i == j):
                #print(i, j)
                continue
            for k in range(5, 10):
                if(j == k or i == k):
                    #print(i, j, k)
                    continue
                for l in range(5, 10):
                    if(l == k or l == j or l == i):
                        #print(i, j, k, l)
                        continue
                    for m in range(5, 10):
                        if(m == l or m == k or m == j or m == i):
                            #print(i, j, k, l, m)
                            continue
                        else:
                            #print("wtf")
                            phase_settings2.append([i, j, k, l, m])
    #print(len(phase_settings2))
    for i in range(0, len(phase_settings)):
        intcode_array.append(0)
        intcode_array[i] = []
        for k in range(0, 5):
            intcode_array[i].append(0)
            intcode_array[i][k] = []
            for j in intcode:
                intcode_array[i][k].append(j.strip())
    #acs(intcode_array, phase_settings)
    acs2(intcode_array, phase_settings2)
    #intcode = run_program(intcode, input)

main()
