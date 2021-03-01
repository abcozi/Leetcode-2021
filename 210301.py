class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        typeLi = set(candyType)
        return min(len(typeLi),len(candyType)//2)