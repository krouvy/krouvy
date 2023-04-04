def get_chunks(src: str, size: int):
    chunks = []
    chunk = []
    for char in src:
        chunk_len = len(chunk)
        if chunk_len < size:
            chunk.append(char)
        elif chunk_len == size:
            chunks.append(chunk)
            chunk = [char]
    if chunk:
        chunks.append(chunk)
    return chunks


class Solution:
    def digitSum(self, s: str, k: int) -> str:
        if len(s) <= k:
            return s
        chunks = get_chunks(src=s, size=k)
        res = "".join(map(str, (sum(map(int, item)) for item in chunks)))
        if len(res) <= k:
            return res
        return self.digitSum(res, k)

s = "11111222223"
k = 3

exm = Solution()
print(exm.digitSum(s, k))
