a = input()
g = a.replace("[","").replace("]","").replace(" ","").replace("(","").replace(")","").split(",")

x = [float(g[0]),float(g[2]),float(g[4]),float(g[6])]
y = [float(g[1]),float(g[3]),float(g[5]),float(g[7])]

#max-min x ardışıksa ve en üst kenarsa
if (min(x) == x[0] and max(x) == x[1]) or (min(x) == x[1] and max(x) == x[2]) or (min(x) == x[2] and max(x) == x[3]) or (min(x) == x[3] and max(x) == x[0]):

    if(y[0] < 0 or y[1] < 0 or y[2] < 0 or y[3] < 0):

        if (min(x) == x[0] == x[2] and y[2] > y[0]) or (min(x) == x[1] == x[3] and y[3] > y[1]):
            area = (max(x) - min(x)) * (abs(y[x.index(max(x))]) + abs(y[x.index(min(x)) + 2])) / 2
            print("%.2f" % area)

        elif (max(x) == x[0] == x[2] and y[2] > y[0]) or (max(x) == x[1] == x[3] and y[3] > y[1]):
            area = (max(x) - min(x)) * (abs(y[x.index(min(x))]) + abs(y[x.index(max(x)) + 2])) / 2
            print("%.2f" % area)

        elif (min(x) == x[0] == x[1]) or (min(x) == x[1] == x[2]) or (min(x) == x[2] == x[3]):
            area = (max(x) - min(x)) * (abs(y[x.index(max(x))]) + abs(y[x.index(min(x)) + 1])) / 2
            print("%.2f" % area)

        elif (max(x) == x[0] == x[3]):
            area = (max(x) - min(x)) * (abs(y[x.index(min(x))]) + abs(y[3])) / 2
            print("%.2f" % area)
        # normal koşullarda
        else:
            area = (max(x) - min(x)) * (abs(y[x.index(max(x))]) + abs(y[x.index(min(x))])) / 2
            print("%.2f" %area)
    #iki max min varsa
    elif (min(x) == x[0] == x[2] and y[2] < y[0]) or (min(x) == x[1] == x[3] and y[3] < y[1]):
        area = (max(x) - min(x)) * (y[x.index(max(x))] + y[x.index(min(x)) + 2]) / 2
        print("%.2f" % area)

    elif (max(x) == x[0] == x[2] and y[2] < y[0]) or (max(x) == x[1] == x[3] and y[3] < y[1]):
        area = (max(x) - min(x)) * (y[x.index(min(x))] + y[x.index(max(x)) + 2]) / 2
        print("%.2f" % area)
    #normal koşullarda
    else:
        area = ((max(x) - x[x.index(min(x)) - 2]) * (y[x.index(max(x))] + y[x.index(min(x)) - 2]) / 2) + ((x[x.index(min(x)) - 2] - x[x.index(min(x)) - 1]) * (y[x.index(min(x)) - 2] + y[x.index(min(x)) - 1]) / 2) + ((x[x.index(min(x)) - 1] - min(x)) * (y[x.index(min(x)) - 1] + y[x.index(min(x))]) / 2)
        print("%.2f" %area)

#max-min x ardışıksa ve en alt kenarsa
elif (min(x) == x[0] and max(x) == x[3]) or (min(x) == x[1] and max(x) == x[0]) or (min(x) == x[2] and max(x) == x[1]) or (min(x) == x[3] and max(x) == x[2]):

    if (y[0] < 0) or (y[1] < 0) or (y[2] < 0) or (y[3] < 0):
        area = ((max(x) - x[x.index(max(x)) - 1]) * (abs(y[x.index(max(x))]) + abs(y[x.index(max(x)) - 1])) / 2) + ((x[x.index(max(x)) - 1] - x[x.index(max(x)) - 2]) * (abs(y[x.index(max(x)) - 1]) + abs(y[x.index(max(x)) - 2])) / 2) + ((x[x.index(max(x)) - 2] - min(x)) * (abs(y[x.index(max(x))- 2]) + abs(y[x.index(min(x))])) / 2)
        print("%.2f" %area)

    elif (min(x) == x[0] == x[3]):
        area = (max(x) - min(x)) * (y[x.index(max(x))] + y[3]) / 2
        print("%.2f" % area)

    elif (max(x) == x[0] == x[1]) or (max(x) == x[1] == x[2]) or (max(x) == x[2] == x[3]):
        area = (max(x) - min(x)) * (y[x.index(min(x))] + y[x.index(max(x)) + 1]) / 2
        print("%.2f" % area)

    else:
        area = (max(x) - min(x)) * (y[x.index(max(x))] + y[x.index(min(x))]) / 2
        print("%.2f" %area)
#max min x ardışık değilse ve negatifse
elif (y[0] < 0) or (y[1] < 0) or (y[2] < 0) or (y[3] < 0):
    area = ((max(x) - x[x.index(max(x)) - 1]) * (abs(y[x.index(max(x))]) + abs(y[x.index(max(x)) - 1])) / 2) + ((x[x.index(max(x)) - 1] - min(x)) * (abs(y[x.index(max(x)) - 1]) + abs(y[x.index(min(x))])) / 2 )
    print("%.2f" %area)
#max min x ardışık değilse
else:
    area = ((max(x) - x[x.index(min(x)) - 1]) * (y[x.index(max(x))] + y[x.index(min(x)) - 1]) / 2) + ((x[x.index(min(x)) - 1] - min(x)) * (y[x.index(min(x)) - 1] + y[x.index(min(x))]) / 2)
    print("%.2f" % area)
