import cv2
import numpy as np

def fill_pos():
    positions = []
    with open('assignment.txt') as fin:
        i=0
        for line in fin.readlines():
            if line[0] == '(':
                line = line.split(',')
                x = line[0].replace('(', '').strip()
                y = line[1].replace(')', '').strip()
                #todo might be y, x instead
                x, y = int(x), int(y)
                positions.append((x,y,i))
                i+=1
    print(max(positions, key=lambda x:x[0]))
    print(max(positions, key=lambda x:x[1]))
    return positions


def merge_row(row):
    output = None
    for num in row:
        image_name = 'images/%s.png' % int(num)
        img = cv2.imread(image_name)

        if output is not None:
            output = np.concatenate((output, img), axis=1)
        else:
            output = img
    return output

def merge(mat):
    final=None
    for row in mat:
        row_img = merge_row(row)
        if final is None:
            final = row_img
        else:
            final = np.concatenate((final, row_img), axis=0)
    return final

mat = np.zeros(shape=(68,68))
positions = fill_pos()

for i in range(len(positions)):
    y, x, line_num =  positions[i]
    mat[y-1][x-1] = line_num

final = merge(mat)

cv2.imwrite('test.png', final)







