class MaxDiff:
    def buySellStockOneTransaction(self, prices):
        """
        Get the largest profit based on input price history when limit to 1 transaction. 

        Example:
            Example 1:
            Input: [7,1,5,3,6,4]
            Output: 5
            Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
                        Not 7-1 = 6, as selling price needs to be larger than buying price.
            
            Example 2:
            Input: [7,6,4,3,1]
            Output: 0
            Explanation: In this case, no transaction is done, i.e. max profit = 0.

        Parameter:
            prices(List[int]): list of integer
        
        Return:
            max_profit(int): max profit with 1 transaction.
        """
        if not prices:
            return 0
        
        cur_min = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            profit = prices[i] - cur_min
            max_profit = max(max_profit, profit)
            cur_min = min(cur_min, prices[i])
        return max_profit

if __name__ == "__main__":
    test = [
        [7,1,5,3,6,4],
        [7,6,5,4,3,2,1]
    ]
    for i in test:
        print(MaxDiff().buySellStockOneTransaction(i))
