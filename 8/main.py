import matplotlib
import matplotlib.pyplot as plt

def read_file():
    f = open("input.txt","r")
    contents = f.read()
    return contents

def find_layer(contents):
    layers = 100
    layer_size = 6*25
    position = 0
    best = 15000
    best1 = 0
    best2 = 0
    for i in range(0, layers):
        counter = 0
        counter1 = 0
        counter2 = 0
        for j in range(0, layer_size):
            digit = contents[position]
            if("0" is digit):
                counter += 1
            elif("1" is digit):
                counter1 += 1
            elif("2" is digit):
                counter2 += 1
            position += 1
        if(best > counter):
            best = counter
            best1 = counter1
            best2 = counter2
    print(best)
    print(best1*best2)
    #print(best[0])
    #print(best[1]*best[2])

    #print(best[0])
    #print(best[1] * best[2])

def render(contents):
    layers = 100
    width = 25
    height = 6
    position = 0
    colors = 'black white'.split()
    cmap = matplotlib.colors.ListedColormap(colors, name='colors', N=None)
    image = [[2 for i in range(0, width)] for j in range(0, height)]
    for layer in range(0, layers):
        for row in range(0, height):
            for column in range(0, width):
                #print(layer, row, column, contents[position], position)
                if(2 is image[row][column]):
                    image[row][column] = int(contents[position])
                position += 1
    plt.imshow(image, cmap=cmap)
    plt.show()




def main():
    contents = read_file()
    find_layer(contents)
    #print(ones*twos)
    render(contents)

main()
