class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        table = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        cList = set()
        for s in words:
            new = ""
            for c in s:
                new+=table[ord(c)-ord('a')]
            cList.add(new)
        return len(cList)