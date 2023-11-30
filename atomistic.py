ROMAN  = ('I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII')
LAYERS = ('s', 'p', 'd', 'f')

# Returns a string of the atom's layers based on Schrodinger's Model.
def getLayers(z):
    # Extends the atomic number l (sub-layer) to ascii based characters.
    def __strLayer(l):
        return (
            LAYERS[l] if l<4 else 
            chr(94+l) if chr(93+l) in LAYERS else 
            chr(93+l)
        )
    
    s, i = '', 0
    while True:
        for j in range((i+1)//2, i+1):
            n = j+1
            l = i-j
            c = 2+l*4
            s += f'{n}{__strLayer(l)} '
            if(z>c):
                s += f'{c}, ' 
                z -= c; continue
            return s + str(z)
        i += 1

# Returns the period's noble element's atomic number, example: period=3, return 18.
def getNobleZ(period):
    return (period**3 + 6*period**2 + 14*period - period%2*(3*period + 6))//6

# Predicats that checks if a given atomic number is Noble.
def isNoble(z):
    return z == getNobleZ(getPeriod(z))

# Returns the number of elements that a given period can hold.
def getPeriodLength(period):
    period -= period%2
    return period*(period//2 + 2) + 2

# Returns the period of a given atomic number.
def getPeriod(z):
    n = 0
    while z>getNobleZ(n): n += 1
    return n

# Returns the group of a given atomic number.
def getGroup(z):
    if z==2: return 18
    period = getPeriod(z)
    group = z-getNobleZ(period-1)
    if group<3: return group
    periodLength = getPeriodLength(period)
    if periodLength>18 and group<periodLength-14: return 3
    return group+18-periodLength

# Returns the number of valence electrons with a given group.
def getValenceByGroup(group):
    return group-7 if group>7 and group<11 else group%10

# Returns the number of valence electrons with a given atomic number.
def getValence(z):
    return getValenceByGroup(getGroup(z))
    
# Returns the Roman symbol of a group with a given atomic number.
def getRomanGroup(z):
    group = getGroup(z)
    return (ROMAN[getValenceByGroup(group)-1] + ('B' if group>2 and group<12 else 'A'))

if __name__ == '__main__':
    # Console test app.
    while True:
        inp = input('Z: ')
        if(inp == ''): break
        z = int(inp)
        print(f'Atomic Number\t: {z}')
        print(f'Valence Electrons: {getValence(z)}')
        print(f'Period\t: {getPeriod(z)}')
        print(f'Group\t: {getGroup(z)} ({getRomanGroup(z)})')
        print(f'Layers\t: {getLayers(z)}\n')
