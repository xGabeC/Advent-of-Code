from functools import reduce

def importFileToArray(filename):
    return [ x.strip() for x in open(filename).readlines() ]


def seperateInputArrayToPassArray(inputArray):
    return " ".join([ "|" if x == "" else x for x in inputArray ]).split("|")


def dictContainsRequiredFields(n):
    return set(['ecl', 'pid', 'hgt', 'eyr', 'hcl', 'byr', 'iyr']).issubset(n.keys())


def seperatePassportToArray(passport):
    return passport.strip().split(" ")


def parseInputToDict(n):
    key_vals = []
    for x in n:
        (key, value) = x.split(":")
        key_vals.append((key, value))
    return (dict(key_vals))


def isValidHGT(n):
    if n[-2:] == "cm":
        return int(n[:-2]) <= 193 and int(n[:-2]) >= 150
    elif n[-2:] == "in":
        return int(n[:-2]) <= 76 and int(n[:-2]) >= 59
    else:
        return False

def isValidHCL(n):
    array = [ char for char in n]
    array.pop(0)
    return n[0] == "#" and set(array).issubset(set(['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']))

def isValidECL(n):
    return n in ['amb','blu','brn','gry','grn','hzl','oth']

def isValidPID(n):
    return len(n) == 9

def isValidBYR(n):
    return int(n) <= 2002 and int(n) >= 1920

def isValidIYR(n):
    return int(n) <= 2020 and int(n) >= 2010

def isValidEYR(n):
    return int(n) <= 2030 and int(n) >= 2020

def isValidPassport(passport):
    return isValidBYR(passport['byr']) and isValidIYR(passport['iyr']) and isValidEYR(passport['eyr']) and isValidHGT(passport['hgt']) and isValidECL(passport['ecl']) and isValidPID(passport['pid']) and isValidHCL(passport['hcl'])





inputArray = importFileToArray('input04.txt')
unvalidatedPassArray = seperateInputArrayToPassArray(inputArray)
unvalidatedPassArray = [ seperatePassportToArray(x) for x in unvalidatedPassArray ]
unvalidatedPassDict = [ parseInputToDict(x) for x in unvalidatedPassArray ]
requiredFieldPassDict = [ x for x in unvalidatedPassDict if dictContainsRequiredFields(x) == True ]

print(len(unvalidatedPassDict))

print(reduce(lambda x, y: x + int(isValidPassport(y)), requiredFieldPassDict, 0))
