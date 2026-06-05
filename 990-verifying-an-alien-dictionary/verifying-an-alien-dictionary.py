class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        lexi = {ch: i for i, ch in enumerate(order)}

        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]

            different = False

            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                    different = True

                    if lexi[w1[j]] > lexi[w2[j]]:
                        return False

                    break

            if not different and len(w1) > len(w2):
                return False

        return True