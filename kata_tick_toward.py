#tick toward completed 1/29/19
#https://www.codewars.com/kata/tick-toward/train/python

def tick_toward(start,target):
    medvals=[start]
    currentpoint=start
    currentx=start[0]
    currenty=start[1]
    while currentpoint != target:
        if currentpoint[0] != target[0]:
            if currentpoint[0]<target[0]:
                currentx+=1
            elif currentpoint[0]>target[0]:
                currentx-=1
        if currentpoint[1] != target[1]: 
            if currentpoint[1]>target[1]: 
                currenty-=1
            elif currentpoint[1]<target[1]:
                currenty+=1
        medvals.insert(medvals.index(currentpoint)+1, (currentx,currenty))
        currentpoint = (currentx, currenty)
    print(medvals)

#better solution:
def tick_toward(start, target):
    x1, y1 = target
    points = [start]
    while points[-1] != target:
        x2, y2 = points[-1]
        a, b = (x2 < x1) - (x2 > x1), (y2 < y1) - (y2 > y1)
        points.append((x2 + a, y2 + b))
    return points
