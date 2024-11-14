from possibleintersections import curves

# given: 2 curves 
def matching(c_1, c_2):
    d_1 = c_1["degree"]
    d_2 = c_2["degree"]
    m_1 = c_1["multiplicity"] + ([1] * (d_1 * d_2))
    m_2 = c_2["multiplicity"] + ([1] * (d_1 * d_2))

    deg_sum = 0
    i = 0
    while (deg_sum < d_1*d_2):
        deg_sum += m_1[i]*m_2[i]
        i += 1
    k = i-1 # number of iterations before they separate

    # if m_i > m_{i+1} check that number of iterations for m_i = m_{i+1} + ... is the same for n_i = n_{i+1} + ...
    i = 1
    iteration = 1
    # while (not m_1[i-1] == 1 and not m_2[i-1] == 1):
    while (iteration < k):
        if (m_1[i] < m_1[i-1]):
            mult_sum = 0
            j = i
            b = 0
            while (not m_1[i-1] == mult_sum):
                mult_sum += m_1[j]
                b += 1
                j += 1
            mult_sum = 0
            j = i
            while (b > 0):
                mult_sum += m_2[j]
                b -= 1
                j += 1
            if (not m_2[i-1] == mult_sum):
                return False, c_1, c_2
        i += 1
        iteration += 1

    # if n_i > n_{i+1} check that number of iterations for n_i = n_{i+1} + ... is the same for m_i = m_{i+1} + ...
    i = 1
    iteration = 1
    # while (not m_1[i-1] == 1 and not m_2[i-1] == 1):
    while (iteration < k):
        # for an 0<= i <= k, if m_i > m_{i+1} and m_i is the sum of the next b terms in the sequence for C1, then also n_i > n_{i+1} and n_i is also the sum of the next b terms in the sequence for C2.
        if (m_2[i] < m_2[i-1]):
            mult_sum = 0
            j = i
            b = 0
            while (not m_2[i-1] == mult_sum):
                mult_sum += m_2[j]
                b += 1
                j += 1
            mult_sum = 0
            j = i
            while (b > 0):
                mult_sum += m_1[j]
                b -= 1
                j += 1
            if (not m_1[i-1] == mult_sum):
                return False, c_1, c_2
        i += 1
        iteration += 1


    # for some k >= 0, we have the equality d1d2 = m_0n_0 + m_1n_1 + ... + m_kn_k (could include into the 1's of the sequences)
    if (deg_sum == d_1*d_2):
        return True, c_1, c_2, k

    return False, c_1, c_2


# TESTING
curve_3 = {
    "parameterization": "(t^2, t^3)",
    "degree": 3,
    "multiplicity": [3]
}

curve_5_1 = {
    "parameterization": "(t^4, t^5)",
    "degree": 5,
    "multiplicity": [5]
}

curve_5_2 = {
    "parameterization": "(t^2, t^{13})",
    "degree": 5,
    "multiplicity": [2] * 6
}

curve_8_2 = {
    "parameterization": "(t^3, t^{22})",
    "degree": 8,
    "multiplicity": [3] * 7
}

def test1(input):
    for i in range(0, len(input)):
        c_1 = input[i]
        for j in range (0, len(input)):
            c_2 = input[j]
            # if (c_2["degree"] == 5):
            result = matching(c_2, c_1)
            if (result[0] and not result[1] == result[2]):
                print(result[1]["degree"], result[1]["parameterization"], result[1]["multiplicity"], " ", result[2]["degree"], result[2]["parameterization"], result[2]["multiplicity"])

def test2():
    for i in range(0, len(curves)):
        c_1 = curves[i]
        result = matching(curve_5_2, c_1)
        if (result[0]):
            print(result[1]["degree"], result[1]["parameterization"], result[1]["multiplicity"], " ", result[2]["degree"], result[2]["parameterization"], result[2]["multiplicity"])


test_set = [
    {
        "parameterization": "(t^2, t^13)",
        "degree": 5,
        "multiplicity": [2] * 6
    },
    {
        "parameterization": "(t^5, t^34)",
        "degree": 13,
        "multiplicity": [5] * 6 + [4]
    },
    {
        "parameterization": "(t^13, t^89)",
        "degree": 34,
        "multiplicity": [13] * 6 + [11] + [2]*5
    },
    {
        "parameterization": "(t^34, t^233)",
        "degree": 89,
        "multiplicity": [34] * 6 + [29] + [5] * 5 + [4]
    },
    {
        "parameterization": "(t^89, t^610)",
        "degree": 233,
        "multiplicity": [89] * 6 + [76] + [13]*5 + [11] + [2]*5
    },
        {
        "parameterization": "(t^233, t^1597)",
        "degree": 610,
        "multiplicity": [233] * 6 + [199] + [34] * 5 + [29] + [5] * 5 + [4]
    }
]

# test1(test_set)

fib_set1 = [
    {
        "parameterization": "(t^2, t^13)",
        "degree": 5,
        "multiplicity": [2] * 6
    },
    {
        "parameterization": "(t^5, t^34)",
        "degree": 13,
        "multiplicity": [5] * 6 + [4]
    },
    {
        "parameterization": "(t^13, t^89)",
        "degree": 34,
        "multiplicity": [13] * 6 + [11] + [2]*5
    },
    {
        "parameterization": "(t^34, t^233)",
        "degree": 89,
        "multiplicity": [34] * 6 + [29] + [5] * 5 + [4]
    },
]

fib_set2 = [
    {
        "parameterization": "(t^4, t^25)",
        "degree": 10,
        "multiplicity": [4] * 6
    },
    {
        "parameterization": "(t^25, t^169)",
        "degree": 65,
        "multiplicity": [25] * 10 + [19] + [6] * 3
    },
    {
        "parameterization": "(t^169, t^1156)",
        "degree": 34*13,
        "multiplicity": [169] * 6 + [142] + [27]*5 + [7]*3 + [6]
    },
    {
        "parameterization": "(t^1156, t^7921)",
        "degree": 89*34,
        "multiplicity": [1156] * 6 + [985] + [171] * 5 + [130] + [41] * 3 + [7] * 5 + [6]
    },
]


test1(fib_set1)
test1(fib_set2)