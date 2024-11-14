
def getMultiplicityArray(m):
    multArray = []
    arr = m.split(',')

    for str in arr:
        str = str.strip()
        if ('_' in str):
            strArr = str.split('_')
            multArray += [int(strArr[0])] * int(strArr[1].strip('{').strip('}'))
        else:
            multArray += [int(str)]
    return multArray

def getCurves():
    curves = []

    # table of curves
    with open('curves.txt', 'r') as f:
        for line in f:
            line = line.replace('\t', ' ').replace('\n', ' ')
            arr = line.split("$")
            curve = {
                "degree": int(arr[0].strip('\ ').strip()),
                "parameterization": arr[1].strip(),
                "multiplicity": getMultiplicityArray(arr[3].strip().strip('(').strip(')'))
            }
            curves.append(curve)

    # 3 to 31
    for d in range(3, 31):
        # all curves
        curve = {
            "degree": int(d),
            "multiplicity": [int(d-1)],
            "parameterization": "(t^{" + str(d-1) + "}, t^{" + str(d) + "})"
        }
        curves.append(curve)

        # even curves
        if (d % 2 == 0):
            curve = {
                "degree": int(d),
                "multiplicity": [int(d/2)] * 3 + [int(d/2)-1],
                "parameterization": "(t^{" + str(int(d/2)) + "}, t^{" + str((2*d)-1) + "})"
            }
            curves.append(curve)

    return curves


curves = getCurves()

def checkMultiplicities(curves):
    for curve in curves:
        d = curve["degree"]
        multiplicity = curve["multiplicity"]
        sum1 = (d-1) * (d-2)
        sum2 = 0
        for m in multiplicity:
            sum2 += m * (m - 1)
        if not sum1 == sum2:
            print(curve)
            print (sum1, sum2)

checkMultiplicities(curves)

# print(curves)