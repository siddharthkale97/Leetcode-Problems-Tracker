'''
322. Coin Change -
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
'''
'''
Approach -
We create a bfs based alogirthm to solve this problem.
Make a visited set, and we push the target "x" in the queue first. We subract each element from the target
and push again to the queue. And after every iteration we increase the depth counter
If no solution return -1, else return depth
'''

class Solution:
	def coinChange(self, coins: List[int], amount: int) -> int:
		# coins.sort()
		# coins = coins[::-1]
		def minNumbers(x, arr, n) :
			q = []
			# Base value in queue
			q.append(x)
			v = set([]) #visited
			d = 0 # depth
			while (len(q) > 0) :
				s = len(q)
				while (s) : # for every level in a tree
					s -= 1
					c = q[0]
					#print(q)
					if (c == 0) :
							return d
					q.pop(0)
					if ((c in v) or c < 0) :
							continue
					# Setting current state as visited
					v.add(c)
					# Pushing the required states in queue
					for i in range(n) :
							q.append(c - arr[i])			
				d += 1
					#print()
					#print(d,c)
			# If no possible solution
			return -1
		
		return minNumbers(amount,coins,len(coins))
'''
Runtime: 3348 ms, faster than 5.02% of Python3 online submissions for Coin Change.
Memory Usage: 15.7 MB, less than 26.16% of Python3 online submissions for Coin Change.
'''