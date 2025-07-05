function solution(n, k) {
    let drinks = Math.max(0, k - Math.floor(n/10))
    return n*12000 + drinks * 2000
}