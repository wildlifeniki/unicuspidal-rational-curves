import math
from multiplicity import euclidean
from getcurves import curves, getMultiplicityArray

def tripleNewtonPairs(degree):
    return generate_mn_list(degree)

def generate_ab_list(degree):
    ab_list = []
    ab_max = degree * 3
    # for a in range(int((degree - 2.18) / 2.62), ab_max+1):
    for a in range(int(degree / 3), ab_max+1):
        bmax = ab_max
        if a > int(degree / 2):
            bmax = int(degree/2)
        for b1 in range(a+1, bmax+1):
            for b2 in range(b1+1, ab_max+1):
                for b3 in range(b2+1, 2*b2-b1+1):
                    ab_list.append((a, b1, b2, b3))
    return ab_list


def generate_mn_list(degree):
    mn_list = []
    ab_list = generate_ab_list(degree)
    parameterizations = []
    for nums in ab_list:
        # parameterization
        a = nums[0]
        b1 = nums[1]
        b2 = nums[2]
        b3 = nums[3]

        # uppercase: check delta invariant
        m1 = a # m_1 * m_2 * m_3
        m2 = math.gcd(m1, b1) # m_2 * m_3
        m3 = math.gcd(m2, b2) # m_3
        n1 = b1 # n_1 * m_2 * m_3
        n2 = b2 - b1 # n_2 * m_3
        n3 = b3 - b2 # n_3

        # lowercase: values in newton pairs (m, n)
        m_3 = m3
        m_2 = int(m2 / m3)
        m_1 = int(m1 / m2)
        n_3 = n3
        n_2 = int(n2 / m3)
        n_1 = int(n1 / m2)

        # semigroup generators
        w1 = m1
        w2 = n1
        w3 = (m_1 * w2) + n2
        w4 = (m_2 * w3) + n3

        # delta invariant
        d_inv = int(((degree - 1) * (degree - 2)))


        if all(i > 1 for i in (m1, m2, m3, m_1, m_2, m_3, n_1, n_2, n_3)):
            if (math.gcd(m_1, n_1) == 1 and math.gcd(m_2, n_2) == 1 and math.gcd(m_3, n_3) == 1):
                pair1 = (m1, n1)
                pair2 = (m2, n2)
                pair3 = (m3, n3)
                # check for duplicate pairs
                if (not pair1 == pair2 and not pair1 == pair3 and not pair2 == pair3):
                    d_inv_check = int(((m1 - 1) * (n1 - 1)) + ((m2 - 1) * n2) + ((m3 - 1) * n3))
                    # check delta invariant
                    if(d_inv == d_inv_check):
                        valid = True
                        semigroup = [0]
                        # check semigroup property
                        for l in range(1, degree-2):
                            semigroup = getSemigroupTriple(w1, w2, w3, w4, l, degree, semigroup)
                            # print(semigroup)
                            compare = (l+1)*(l+2)/2
                            if(len(semigroup) != compare):
                                valid = False
                        if(valid):
                            parameterizations.append([a, b1, b2, b3])
                            mn_list.append((pair1, pair2, pair3))
    return parameterizations

def getSemigroupTriple(w1, w2, w3, w4, l, degree, semigroup):
    maxVal = l * degree
    for num in semigroup:
        num1 = num + w1
        num2 = num + w2
        num3 = num + w3
        num4 = num + w4
        if(num1 not in semigroup and num1 <= maxVal):
            semigroup.append(num1)
            semigroup.sort()
        if(num2 not in semigroup and num2 <= maxVal):
            semigroup.append(num2)
            semigroup.sort()
        if(num3 not in semigroup and num3 <= maxVal):
            semigroup.append(num3)
            semigroup.sort()
        if(num4 not in semigroup and num4 <= maxVal):
            semigroup.append(num4)
            semigroup.sort()
        if (num1 > maxVal and num2 > maxVal and num3 > maxVal and num4 > maxVal):
            return semigroup

def multiplicitySequence(m, b1, b2, b3):
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
    
    output = ""
    nums = [1]
    for i in sequence:
        if i not in nums:
            count = sequence.count(i)
            if count == 1:
                output += str(i) + ", "
            else:
                output += str(i) + "_" + str(count) + ", "
            nums.append(i)
    return "" + output[:-2]

# curves2 = []
# for num in range(41, 42):
#     print("degree: " + str(num))
#     parameterizations = tripleNewtonPairs(num)
#     for parameterization in parameterizations:
#         curve = {
#             "degree": num,
#             "multiplicity": getMultiplicityArray(multiplicitySequence(parameterization[0], parameterization[1], parameterization[2], parameterization[3])),
#             "parameterization": "(t^{" + str(parameterization[0]) + "}, t^{" + str(parameterization[1]) + "} + t^{" + str(parameterization[2]) +"} +} t^{" + str(parameterization[3]) +"})"
#         }
#         curves2.append(curve)
#         # print(curve)

#     # print("parameterizations for ", num)
#     # print(tripleNewtonPairs(num))

# print(curves2)