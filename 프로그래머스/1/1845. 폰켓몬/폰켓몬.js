function solution(nums) {
  const map = new Map();
  nums.forEach((value) => {
    map.set(value, (map.get(value) || 0) + 1);
  });

  return Math.min(map.size, nums.length/2);
}