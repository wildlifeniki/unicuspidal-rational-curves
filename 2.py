import math

def fourNewtonPairs(degree):
    ab_max = int(((degree - 1) * (degree - 2)) / 2)
    return generate_mn_list(ab_max, degree)

def generate_ab_list(ab_max):
    ab_list = []
    for b1 in range(2, ab_max+1):
        for b2 in range(b1+1, ab_max+1):
            for b3 in range(b2+1, ab_max+1):
                for b4 in range(b3+1, ab_max+1):
                    ab_list.append((b1, b2, b3, b4))
    return ab_list

def generate_mn_list(ab_max, degree):
    mn_list = []
    ab_list = generate_ab_list(ab_max)
    for nums in ab_list:
        #parameterization
        b1 = nums[0]
        b2 = nums[1]
        b3 = nums[2]
        b4 = nums[3]

        # uppercase: check delta invariant
        m1 = 16
        m2 = 8
        m3 = 4
        m4 = 2
        n1 = b1 # n_1 * m_2 * m_3 * m_4
        n2 = b2 - b1 # n_2 * m_3 * m_4
        n3 = b3 - b2 # n_3 * m_4
        n4 = b4 - b3 # n_4

        # lowercase: values in newton pairs (m, n)
        m_4 = m4
        m_3 = int(m3 / m4)
        m_2 = int(m2 / m3)
        m_1 = int(m1 / m2)
        n_4 = n4
        n_3 = int(n3 / m4)
        n_2 = int(n2 / m3)
        n_1 = int(n1 / m2)

        # semigroup generators
        w1 = m1
        w2 = n1
        w3 = (m_1 * w2) + n2
        w4 = (m_2 * w3) + n3
        w5 = (m_3 * w4) + n4

        # delta invariant
        d_inv = int(((degree - 1) * (degree - 2)))
        
        if all(i > 1 for i in (m1, m2, m3, m4, m_1, m_2, m_3, m_4, n_1, n_2, n_3, n_4)):
            if (math.gcd(m_1, n_1) == 1 and math.gcd(m_2, n_2) == 1 and math.gcd(m_3, n_3) == 1 and math.gcd(m_4, n_4) == 1):
                pair1 = (m1, n1)
                pair2 = (m2, n2)
                pair3 = (m3, n3)
                pair4 = (m4, n4)
                # check for duplicate pairs
                if (not pair1 == pair2 and not pair1 == pair3 and not pair2 == pair3 and not pair4 == pair1 and not pair4 == pair2 and not pair4 == pair3):
                    d_inv_check = int(((m1 - 1) * (n1 - 1)) + ((m2 - 1) * n2) + ((m3 - 1) * n3) + ((m4 - 1) * n4))
                    # check delta invariant
                    if(d_inv == d_inv_check):
                        valid = True
                        print(valid, pair1, pair2, pair3, pair4)

                        semigroup = [0]
                        # check semigroup property
                        for l in range(1, degree-2):
                            semigroup = getSemigroup(w1, w2, w3, w4, w5, l, degree, semigroup)
                            compare = (l+1)*(l+2)/2
                            if(len(semigroup) != compare):
                                valid = False
                        if(valid):
                            mn_list.append((pair1, pair2, pair3, pair4))
                            # print("a:", a, "b:", b1, b2, b3)
                            # print("(m, n):", (m_1, n_1), (m_2, n_2), (m_3, n_3))
    return mn_list


def getSemigroup(w1, w2, w3, w4, w5, l, degree, semigroup):
    maxVal = l * degree
    for num in semigroup:
        num1 = num + w1
        num2 = num + w2
        num3 = num + w3
        num4 = num + w4
        num5 = num + w5
        if(num1 not in semigroup and num1 <= maxVal):
            i = findIndex(num5, semigroup)
            semigroup.insert(i, num1)
        if(num2 not in semigroup and num2 <= maxVal):
            i = findIndex(num5, semigroup)
            semigroup.insert(i, num2)
        if(num3 not in semigroup and num3 <= maxVal):
            i = findIndex(num5, semigroup)
            semigroup.insert(i, num3)
        if(num4 not in semigroup and num4 <= maxVal):
            i = findIndex(num5, semigroup)
            semigroup.insert(i, num4)
        if(num5 not in semigroup and num5 <= maxVal):
            i = findIndex(num5, semigroup)
            semigroup.insert(i, num5)
        if (num1 > maxVal and num2 > maxVal and num3 > maxVal and num4 > maxVal and num5 > maxVal):
            return semigroup


def findIndex(num, semigroup):
    for i, e in reversed(list(enumerate(semigroup))):
        print(i, e, num)
        if (num >= e):
            return i+1

for num in range(24, 25):
    print("pairs for", num)
    print(fourNewtonPairs(num))