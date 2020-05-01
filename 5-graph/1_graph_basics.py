class GraphAsAdjList:
    def __init__(self):
       self.nodes = []
        

class GraphAsAdjMatrix:
    def __init__(self):
        self.graph = [[]]


class Node:
    def __init__(self, val = -1):
        self.neighbors = []
        self.val = val


class FindJudge:
    """
    Leetcode 997. Find the Town Judge    
    """
    def findJudge(self, N, trust):
        """
        Find town judge among n people based on trust relationship. Judge should be trust by everyone but trusts no one.

        Parameters:
            N(int): n peoples from 1 to N
            trust(List[List[int]]): array of trust relationship. [a, b] means a trusts b
        
        Returns:
            res(int): index of judge. Return -1 if none of them qualifies            
        """
        if not trust:
            return -1
        
        # construct graph
        # people_arr[y][x] means y trust x
        people_arr = [[[] for i in range(N + 1)] for j in range(N + 1)]
        for y, x in trust:
            people_arr[y][x] = 1
                    
        # find judge
        # people_arr[][x] -> people trust x, people_arr[x][] -> people that x trust
        judge = 0
        for i in range(1, N + 1):
            trusted_by_people, trust_people = self.trustRelationship(i, people_arr)
            if trusted_by_people and not trust_people:
                if judge == 0:
                    judge = i
                else:
                    return -1

        return judge if judge != 0 else -1

    def trustRelationship(self, i, people_arr):
        N = len(people_arr)  
        trusted_by_people = True
        trust_people = False
        for people in range(1, N):
            if people == i:
                continue
            if people_arr[people][i] != 1:
                trusted_by_people = False
            if people_arr[i][people] == 1:
                trust_people = True
        return (trusted_by_people, trust_people)

    def findJudge2(self, N, trust):
        # corner case
        if len(trust) == 0 and N == 1:
            return N
        if len(trust) == 0 and N != 1:
            return -1

        truster = {x[0] for x in trust}
        truster_number = [0 for i in range(N + 1)]        
        for x in trust:
            truster_number[x[1]] += 1
        
        candidate = []
        for i in range(1, N + 1):
            if truster_number[i] == N - 1:
                candidate.append(i)
                
        if len(candidate) != 1:
            return -1
        return candidate[0] if candidate[0] not in truster else -1
            


if __name__ == "__main__":
    test = [
        (2, [[1,2]]),
        (3, [[1,3],[2,3]]),
        (3, [[1,3],[2,3],[3,1]]),
        (3, [[1,2],[2,3]])
    ]
    for n, trust in test:
        print(FindJudge().findJudge2(n, trust))