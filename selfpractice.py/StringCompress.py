class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        if len(chars) < 2:
            return len(chars)
        
        write_index = read_index = 0

        while read_index < len(chars):
            curr_char = chars[read_index]
            count = 1
            while read_index < len(chars) - 1 and chars[read_index] == chars[read_index + 1]:
                count += 1
                read_index += 1

            chars[write_index] = curr_char
            write_index += 1

            if count > 1:
                for digit in str(count):
                    chars[write_index] = digit
                    write_index += 1

            read_index += 1

        return write_index

sol = Solution()
chars = ["a", "z", "z", "c", "c", "c"]
print(sol.compress(chars))

        