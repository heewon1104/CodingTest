function solution(clothes) {
  const result = new Map();
  clothes.forEach((v) => {
    const arr = result.get(v[1]) || [];
    result.set(v[1], arr.concat(v[0]));
  });

  let answer = 1;
  for (const [type, items] of result) {
    answer *= items.length + 1;
  }

  return answer - 1;
}