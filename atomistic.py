def strLayer(l):
    return (
        LAYERS[l] if l<4 else 
        chr(94+l) if chr(93+l) in LAYERS else 
        chr(93+l)
    )
    
def getLayers(z):
    s, i = '', 0
    while True:
        for j in range((i+1)//2, i+1):
            n = j+1
            l = i-j
            c = 2+l*4
            s += f'{n}{strLayer(l)} '
            if(z>c):
                s += f'{c}, ' 
                z -= c; continue
            return s + str(z)
        i += 1

def getNobleZ(n):
    return (n**3 + 6*n**2 + 14*n - n%2*(3*n + 6))//6

def isNoble(z):
    return z == getNobleZ(getPeriod(z))

def getPeriodLength(period):
    period -= period%2
    return period*(period//2 + 2) + 2

def getPeriod(z):
    n = 0
    while z>getNobleZ(n): n += 1
    return n

def getGroup(z):
    if z==2: return 18
    period = getPeriod(z)
    group = z-getNobleZ(period-1)
    if group<3: return group
    periodLength = getPeriodLength(period)
    if periodLength>18 and group<periodLength-14: return 3
    return group+18-periodLength

def getValenceByGroup(group):
    return group-7 if group>7 and group<11 else group%10

def getValence(z):
    return getValenceByGroup(getGroup(z))

def getRomanGroup(z):
    group = getGroup(z)
    return (ROMAN[getValenceByGroup(group)-1] + ('B' if group>2 and group<12 else 'A'))

def logAtom(z):
    print(f'Atomic Number\t: {z}')
    print(f'Valence Electrons: {getValence(z)}')
    print(f'Period\t: {getPeriod(z)}')
    print(f'Group\t: {getGroup(z)} ({getRomanGroup(z)})')
    print(f'Layers\t: {getLayers(z)}')

ROMAN  = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII']
LAYERS = ['s', 'p', 'd', 'f']

if __name__ == '__main__':
    while True:
        inp = input('Z: ')
        if(inp == ''): break
        logAtom(int(inp))
        print()