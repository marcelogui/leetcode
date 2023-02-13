class Solution:
    def countOdds(self, low: int, high: int) -> int:
        diff = high = low
        num_odds = diff // 2
        if low % 2 == 1 or high % 2 == 1:
            return num_odds + 1
        else:
            return num_odds



