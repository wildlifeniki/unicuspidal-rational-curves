# get multiplicity sequence given x^m = y^b1 + y^b2 + y^b3 (for less than n b, bn = 1)
# output in latex math
def multiplicitySequence(m, b1, b2, b3, latex = False):
    sequence = []

    values1 = euclidean(b1, m)
    for pair in values1:
        sequence.extend([pair[1]]*pair[0])

    if not b2 == 0:
        m2 = values1[-1][1]
        values2 = euclidean(b2-b1, m2)
        for pair in values2:
            sequence.extend([pair[1]]*pair[0])

        if not b3 == 0:
            m3 = values2[-1][1]
            values3 = euclidean(b3-b2, m3)
            for pair in values3:
                sequence.extend([pair[1]]*pair[0])
    
    latex_output = ""
    array_output = []
    nums = [1]
    for i in sequence:
        if i not in nums:
            count = sequence.count(i)
            if latex:
                if count == 1:
                    latex_output += str(i) + ", "
                else:
                    latex_output += str(i) + "_" + str(count) + ", "
            else:
                    array_output += [i]
            nums.append(i)
    if latex:
        return "$(" + latex_output[:-2] + ")$"
    else:
        return array_output
    

# euclidean algorithm
def euclidean(x, y):
    values = []
    while not y == 0:
        # x = qy + r
        q = int(x/y)
        r = int(x % y)
        values.append((q, y))
        x = y
        y = r
    return values
