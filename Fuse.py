
    

def fuse(pokemon):
    """
		Function description: This function returns an output integer containing the largest possible combination of a fusemon in an order given

		Approach description: This is a dynamic programming problem. The approach was to essentailly have it that any given combination of a fitmon is the best combination, eg ABC and DE combine, this will be the best combination of ABC not just any ABC.
        It continualy uses the best combination obtained when combining elements. Eg (a(bc)) and (ab(c)) are two combos that both result in abc, this dynamic programming solution will only take the best of those two when taking into consdiertions that use abc.

		Input: 
			pokemon: an array based list containing lists of size three, in which postion 0 and 2 is a float between 0.1 and 0.9 (inclusive), and position one is an integer, positive
		
		Output: an integer that represtent the optimal order combination that can be achieved when fusing pokemon
		
		Time complexity: O(n^3), where n is the amount of elements in the pokemon list

		Time complexity analysis : No search or sort algorthims are here, so the time complexity is purerly its own. While the first loop is the size of the list -1, (n)
        it contains a for loop that is n - index1 (index pf first loop), this is a constant, so therefore its n. the third for loop is also n, while slightly less than n in reality, would simplify to n given infinitely large solutions.
        (n-1)*(n*logn)*(n*logn) = n^3

		Space complexity: O(n^2),  where n is the number of elements in the pokemon (input) array

		Space complexity analysis: A table is created that uses the the pokemon input array and squares it, therefore n*n = n^2
		
	"""


    table = [[0 for _ in range(len(pokemon))] for _ in range(len(pokemon))]
    for i in range(len(table)):
        table[i][i] = pokemon[i]
    for diagonal in range(1, len(table)):
        for i in range(len(table) - diagonal):
            max = [0,0,0]
        
            for k in range(diagonal):
            
                if max[1] < table[i][k + i][2]*table[i][k + i][1] + table[i+k +1][diagonal + i][0]*table[i+k + 1][diagonal+ i][1]:
                    max = [table[i][k + i][0], int(table[i][i+k][2]*table[i][i+k][1] + table[i+k+1][diagonal+i][0]*table[i+1+k][diagonal+i][1]), table[1+i+k][diagonal+i][2]]
        
            table[i][i + diagonal] = max
        
        
    return table[0][len(table) -1][1]
    
    


