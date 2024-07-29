class Solution:
    def compress(self, chars: List[str]) -> int:
        index = 0 # position in the list where next character or count will be written
        i = 0 #iterate through the list of characters

        while i < len(chars):
            j = i
            while j < len(chars) and chars[j] == chars[i]: # iterates as long as char at position j are == char at i
                j += 1

            chars[index] = chars[i] # character at position i is written to curent index position
            index += 1 # then increment index
            if j - i > 1: # if the sequence length is greater than 1,
                count = str(j - i) # convert to a string
                for c in count: 
                    chars[index] = c 
                    index += 1

            i = j # i is updated to j to move to the next sequence of characters

        return index
