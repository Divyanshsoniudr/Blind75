class Solution:
    def encode(self, strs):
        return ''.join([str(len(s)) + ":;" + s for s in strs])

    def decode(self, s):
        decoded = []
        i = 0
        while i < len(s):
            delimiter_index = s.find(":;", i)
            length = int(s[i:delimiter_index])
            decoded.append(s[delimiter_index + 2:delimiter_index + 2 + length])
            i = delimiter_index + 2 + length
        return decoded
