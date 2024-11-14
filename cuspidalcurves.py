import math

def singleNewtonPairs(degree):
    pairs = []
    d_inv = int(((degree - 1) * (degree - 2)))

    for m in range(1, degree * degree):
        for n in range(m, degree * degree):
            d_inv_check = ((m - 1) * (n - 1))
            if (d_inv_check == d_inv):
                valid = True
                for l in range(1, 4):
                    semigroup = getSemigroup(m, n, l, degree)
                    compare = (l+1)*(l+2)/2
                    if(len(semigroup) != compare):
                        valid = False
                if(valid):
                    pairs.append((m, n))

    return pairs

def getSemigroup(a, b, l, degree):
    semigroup = [0]
    maxVal = l * degree
    for num in semigroup:
        numa = num + a
        numb = num + b
        if (numa not in semigroup and numa <= maxVal):
            semigroup.append(numa)
            semigroup.sort()
        if (numb not in semigroup and numb <= maxVal):
            semigroup.append(numb)
            semigroup.sort()
        if (numa > maxVal and numb > maxVal):
            return semigroup

def tripleNewtonPairs(degree):
    ab_max = int(((degree - 1) * (degree - 2)) / 2)
    return generate_mn_list(ab_max, degree)

def generate_ab_list(ab_max):
    ab_list = []
    for a in range(2, ab_max+1):
        for b1 in range(a+1, ab_max+1):
            for b2 in range(b1+1, ab_max+1):
                for b3 in range(b2+1, ab_max+1):
                    ab_list.append((a, b1, b2, b3))
    return ab_list

def generate_mn_list(ab_max, degree):
    mn_list = []
    ab_list = generate_ab_list(ab_max)
    for nums in ab_list:
        #parameterization
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

        # check kodaira dimension = 2
        if (m_1 + n_1 + n_2 + n_3 > 3 * degree + 1):

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
                                mn_list.append((pair1, pair2, pair3))
                                # print("a:", a, "b:", b1, b2, b3)
                                # print("(m, n):", (m_1, n_1), (m_2, n_2), (m_3, n_3))
    return mn_list

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


# num = 16
# print(tripleNewtonPairs(num))

for num in range(25, 30):
    print("pairs for", num)
    print(tripleNewtonPairs(num))