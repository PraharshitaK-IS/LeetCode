#https://leetcode.com/problems/minimum-genetic-mutation/
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank_set = set(bank)
        if endGene not in bank_set:
            return -1

        gene_options = ['A', 'C', 'G', 'T']
        queue = deque([(startGene, 0)])
        visited = set([startGene])

        while queue:
            current, mutations = queue.popleft()
            if current == endGene:
                return mutations

            for i in range(len(current)):
                for char in gene_options:
                    if char != current[i]:
                        mutated = current[:i] + char + current[i+1:]
                        if mutated in bank_set and mutated not in visited:
                            visited.add(mutated)
                            queue.append((mutated, mutations + 1))
        return -1