const ROMAN  = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII']
const LAYERS = ['s', 'p', 'd', 'f']

// Returns a string of the atom's layers based on Schrodinger's Model.
function getLayers(z){
    // Extends the atomic number l (sub-layer) to ascii based characters.
    function __strLayer(l){
        return (
            l<4? LAYERS[l] : 
            LAYERS.includes(String.fromCharCode(93+l))? 
            String.fromCharCode(94+l) : 
            String.fromCharCode(93+l)
        )
    }
    let s = '', i = 0
    while(true){
        for (j = Math.ceil((i+1)/2); j<i+1; j++){
            const n = j+1, l = i-j, c = 2+l*4
            s += `${n}${__strLayer(l)} `
            if(z>c){
                s += `${c}, `
                z -= c; continue
            }
            return s + z
        }
        i += 1
    }
}
// Returns the period's noble element's atomic number, example: period=3, return 18.
function getNobleZ(period){
    return (period**3 + 6*period**2 + 14*period - period%2*(3*period + 6))//6
}
// Predicat that checks if a given atomic number is Noble.
function isNoble(z){
    return z == getNobleZ(getPeriod(z))
}
// Returns the number of elements that a given period can hold.
function getPeriodLength(period){
    period -= period%2
    return period*(period/2 + 2) + 2
}
// Returns the period of a given atomic number.
function getPeriod(z){
    let n = 0
    while(z>getNobleZ(n)) n++
    return n
}
// Returns the group of a given atomic number.
function getGroup(z){
    if(z==2) return 18
    const period = getPeriod(z)
    const group = z-getNobleZ(period-1)
    if(group<3) return group
    const periodLength = getPeriodLength(period)
    return periodLength>18 && group<periodLength-14? 3 : group+18-periodLength
}
// Returns the number of valence electrons with a given group.
function getValenceByGroup(group){
    return group>7 && group<11? group-7 : group%10
}
// Returns the number of valence electrons with a given atomic number.
function getValence(z){
    return getValenceByGroup(getGroup(z))
}
// Returns the Roman symbol of a group with a given atomic number.
function getRomanGroup(z){
    const group = getGroup(z)
    return (ROMAN[getValenceByGroup(group)-1] + (group>2 && group<12? 'B' : 'A'))
}
// Test function.
function logAtom(z){
    console.log(`Atomic Number (Z): ${z}`)
    console.log(`Valence Electrons: ${getValence(z)}`)
    console.log(`Period: ${getPeriod(z)}`)
    console.log(`Group : ${getGroup(z)} (${getRomanGroup(z)})`)
    console.log(`Layers: ${getLayers(z)}\n`)
}
