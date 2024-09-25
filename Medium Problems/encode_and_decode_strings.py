class Codec:
    def encode(self, strs: List[str]) -> str:
        running = ""
        for i in range(len(strs)):
            running+=strs[i]
            if i!=len(strs)-1:
                running+="é"
        return running
        """Encodes a list of strings to a single string.
        """
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        l = s.split("é")
        return l

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
