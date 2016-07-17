matrix = []
rules = []


def prep():
    matrix = []
    rules = []

def reduce(str):
    if len(str)==2:
        if str[1] == ' ' or str[1] == '\n':
            return str[:-1]
    return str

def matrix_from_file(filepath):
    f = open(filepath, 'r')
    ss = list(f)
    f.close()
    n = 2
    for str in ss:
        matrix[len(matrix):] = [[reduce(str[i:i+n]) for i in range(0, len(str), n)]]

def rules_from_file(filepath):
    f = open(filepath, 'r')
    ss = list(f)
    f.close()
    for d in ss:
        d = "".join(d.split('\n'))
        g = d.split("->")
        h = g[1].split("|")
        for k in h:
            rules[len(rules):] = [[g[0], k]]

def alg(sg):
    prep()
    s = sg + "#"
    m = "#"
    step(s, m, 0)

def step(s, m, n):
    x = m[-1]
    y = s[n]
    print ('{0:15} ==> {1:10}'.format(s[:n] + ' !' + s[n:], m))
    if len(s)>n:
        i = geti(y)
        j = getj(x)
        sign = getsign(i, j)
        if sign == -1:
            ex("sentence is incorrect")
            return
        if sign == 'F':
            if m == "#E":
                print("success!")
            else:
                print("sentence is incorrect")
            return
        if sign == "<" or sign == "<=" or sign == "=":
            ##transfer
            step(s, m + y, n+1)
            return
        else:
            if sign == ">":
                ##wrap
                t, m = wrap(m)
                if t:
                    step(s, m, n)
                    return
                else:
                    ex("sentence is incorrect")
                    return
            else:
                ex("sentence is incorrect")

def geti(x):
    i = 0
    for v in matrix[0]:
        if v == x:
            return i
        i = i+1
    return -1

def getj(y):
    j = 0
    for v in matrix:
        if v[0] == y:
            return j
        j = j+1
    return -1

def getsign(i, j):
    if not(len(matrix[j])>i) or i==-1 or j==-1:
        return -1
    return matrix[j][i]

def wrap(m):
    for r in rules:
        if m.endswith(r[1]):
            m = m[:-len(r[1])]+r[0]
            return True, m
    return False, m

def ex(mes):
    print("error occurred:\n\t" + mes)

def print_matrix():
    print ("matrix:")
    for vec in matrix:
        w = ""
        for v in vec:
            w = w + '{0:3}'.format(v)
        print (w)
    print("\n")

def print_rules():
    print ("rules:")
    for vec in rules:
        print('{0}->{1:5}'.format(vec[0],vec[1]))
    print("\n")


matrix_from_file("mat.txt")
print_matrix()
rules_from_file("rul.txt")
print_rules()

alg("a+a*(a*a)")




