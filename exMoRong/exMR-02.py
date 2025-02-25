s = '-100#^adfkj8902w3ir021@swf-20'

print("s: ", len(s))
def laysoduong(s):
    d = 0
    i=0
    while i < len(s) :
        print(f"s[{i}] = {s[i]}")
        if s[i] >= '0' and s[i] <= '9' :
            z = int(s[i])
            j = i + 1
            print("j : ", j, f"S[{i}] = {z}")
            while j < len(s):
                print("sdhafvjbjJHKBANASGBH")
                if s[j] >= '0' and s[j] <= '9':
                    z = z*10 + int(s[j])
                    if j==len(s)-1 :
                        d = d+z
                        i=j
                        break
                else :
                    print("z : ", z)
                    d = d + z
                    i = j-1
                    break
                j = j + 1
        i=i+1
    return  d

print("số dưng : ", laysoduong(s))


def laysoam(s):
    d = 0
    i=0
    while i < len(s):
        print(f"s[{i}] = {s[i]}")
        if s[i+1] >= '0' and s[i+1] <= '9' and s[i] =='-' :
            z = int(s[i+1])
            j = i + 2
            while j < len(s):
                if s[j] >= '0' and s[j] <= '9':
                    z = z * 10 + int(s[j])
                    if j == len(s) - 1:
                        d = d - z
                        i = j
                        break
                else:
                    d = d - z
                    i = j - 1
                    break
                j = j + 1
        i = i + 1
    return d
print("số + : ", laysoduong(s) , " - số - : ", laysoam(s))

