function solution(participant, completion) { 
    const map = new Map();
    
    participant.forEach((v) => {
        map.set(v, (map.get(v) || 0) + 1)
    })
    completion.forEach((v) => {
        map.set(v, map.get(v) - 1)
    })
    
    for(let [key, value] of map){
        if(value > 0)
            return key
    }
}