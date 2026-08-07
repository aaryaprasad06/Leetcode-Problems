class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters= {
            2: 'abc',
            3: 'def',
            4: 'ghi',
            5: 'jkl',
            6: 'mno',
            7: 'pqrs',
            8: 'tuv',
            9: 'wxyz'
        }
        result= []
        path= []

        def f(idx):
            if len(path)== len(digits):
                result.append("".join(path))
                return
            selected= int(digits[idx])
            choices= letters[selected]
            for ch in choices:
                path.append(ch)
                f(idx+1)
                path.pop()
        
        f(0)
        return result