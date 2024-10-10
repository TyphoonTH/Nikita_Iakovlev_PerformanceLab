circle_file, points_file=input(), input()

with open(circle_file,"r") as circle:
    circle_data=circle.read().split('\n')
    
center, radius=[float(i) for i in circle_data[0].split()],float(circle_data[1])

with open(points_file,"r") as points:
    for line in points:
        point=[float(i) for i  in line.split()]
        if (point[0]-center[0])**2+(point[1]-center[1])**2<radius**2:
            print(1)
        elif (point[0]-center[0])**2+(point[1]-center[1])**2==radius**2:
            print(0)   
        else:
            print(2)    
