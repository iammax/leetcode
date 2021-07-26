class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        richest_balance = 0
        
        for i in range(len(accounts)):
            balance = sum(accounts[i])
            if balance > richest_balance:
                richest_balance = balance
                
        return richest_balance
