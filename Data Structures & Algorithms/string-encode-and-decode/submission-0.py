class Solution:

    def encode(self, strs: List[str]) -> str:
        encode = ""
        for i in range(len(strs)):
            encode = encode + str(len(strs[i]) // 100)
            encode = encode + str((len(strs[i]) // 10) % 10)
            encode = encode + str(len(strs[i]) % 10)
            encode = encode + strs[i]
        
        return encode

    def decode(self, s: str) -> List[str]:
        track = 0
        decode = []

        while track != len(s):
            hun = s[track]
            tens = s[track + 1]
            ones = s[track + 2]
            length = 100 * int(hun) + 10 * int(tens) + int(ones)

            decode.append(s[track + 3 : track + 3 + length])

            track = track + 3 + length
        
        return decode