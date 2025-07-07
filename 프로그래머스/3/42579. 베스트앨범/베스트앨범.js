function solution(genres, plays) {
    const map = new Map()
    genres.forEach((v, idx) => {
        map.set(v, (map.get(v) || 0) + plays[idx])
    })
    const arr = [...map]
    arr.sort((a,b) => b[1]-a[1])
    
    const answer = []
    for(let [genre, totalPlay] of arr){
        let tmpArr = []
        for(let i = 0; i<genres.length; i++){
            if(genres[i] === genre){
                tmpArr.push([i, plays[i]])
            }
        }
        tmpArr.sort((a,b) => (b[1]-a[1]))
        for(let i = 0; i<Math.min(tmpArr.length, 2); i++){
            answer.push(tmpArr[i][0])
        }
    }
    return answer;
}