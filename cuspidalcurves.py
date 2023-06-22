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

def tripleNewtonPairs_old(degree):
    # generate a < b1 < b2 < b3
    # use them to generate M1, M2, M3, N1, N2, N3
        # M1, M2, M3 > 1
        # no duplicate pairs
    # calculate delta invariant
    # return pairs that match invariant
    final_pairs = []
    d_inv = int(((degree - 1) * (degree - 2)))
    all_pairs = generate_mn_list(100, degree)
    for pairs in all_pairs:
        m1 = pairs[0][0]
        n1 = pairs[0][1]
        m2 = pairs[1][0]
        n2 = pairs[1][1]
        m3 = pairs[2][0]
        n3 = pairs[2][1]
        d_inv_check = int(((m1 - 1) * (n1 - 1)) + ((m2 - 1) * n2) + ((m3 - 1) * n3))
        if(d_inv == d_inv_check):
            final_pairs.append(pairs)
    return final_pairs

def tripleNewtonPairs(degree):
    abmax = int(((degree - 1) * (degree - 2)) / 2)
    return generate_mn_list(abmax, degree)

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
        a = nums[0]
        b1 = nums[1]
        b2 = nums[2]
        b3 = nums[3]
        #upper
        m1 = a
        m2 = math.gcd(m1, b1)
        m3 = math.gcd(m2, b2)
        n1 = b1
        n2 = b2 - b1
        n3 = b3 - b2

        #lower
        m_3 = m3
        m_2 = int(m2 / m3)
        m_1 = int(m1 / m2)
        n_3 = n3
        n_2 = int(n2 / m3)
        n_1 = int(n1 / m2)


        w1 = m1
        w2 = n1
        w3 = (m_1 * w2) + n2
        w4 = (m_2 * w3) + n3

        d_inv = int(((degree - 1) * (degree - 2)))

        if (m1 > 1 and m2 > 1 and m3 > 1 and m_1 > 1 and m_2 > 1 and m_3 > 1 and n_1 > 1 and n_2 > 1 and n_3 > 1):
            if (math.gcd(m_1, n_1) == 1 and math.gcd(m_2, n_2) == 1 and math.gcd(m_3, n_3) == 1):
                pair1 = (m1, n1)
                pair2 = (m2, n2)
                pair3 = (m3, n3)
                if (not pair1 == pair2 and not pair1 == pair3 and not pair2 == pair3):
                    d_inv_check = int(((m1 - 1) * (n1 - 1)) + ((m2 - 1) * n2) + ((m3 - 1) * n3))
                    if(d_inv == d_inv_check):
                        valid = True
                        semigroup = [0]
                        for l in range(1, degree-2):
                            semigroup = getSemigroupTriple(w1, w2, w3, w4, l, degree, semigroup)
                            print(semigroup)
                            compare = (l+1)*(l+2)/2
                            if(len(semigroup) != compare):
                                valid = False
                        if(valid):
                            mn_list.append((pair1, pair2, pair3))
                            print("a:", a, "b:", b1, b2, b3)
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


# num = 19

# print(tripleNewtonPairs(12))

# for num in range(20, 31):
#     print("pairs for", num)
#     print(tripleNewtonPairs(num))

# def wcheck():
#     #upper
#         m1 = 8
#         m2 = 4
#         m3 = 2
#         n1 = 12
#         n2 = 6
#         n3 = 3

#         #lower
#         m_3 = 2
#         m_2 = 2
#         m_1 = 2
#         n_3 = 15
#         n_2 = 3
#         n_1 = 3

#         w1 = m1
#         w2 = n1
#         w3 = (m_1 * w2) + n2
#         w4 = (m_2 * w3) + n3

#         print(w1, w2, w3, w4)

#         print(getSemigroupTriple(w1, w2, w3, w3, 4, num, [0]))

# wcheck()

#print(singleNewtonPairs(num))

#print(getSemigroup(2, 13, 3, 5))
print (8**3 % 9)