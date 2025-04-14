class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_string = ''
        longest_string_count = 0
        string_len = len(s)

        for i in range(string_len):
            #odd length palindrome
            count = 0

            while (i - count) >= 0 and (i + count) < string_len:
                if s[i - count] == s[i + count]:
                    count += 1
                else:
                    break
            if (1 + 2 * count) > longest_string_count:
                longest_string_count = (1 + 2 * count)
                longest_string = s[(i + 1 - count):(i + count)]
        
            #even length palindrome
            count = 0

            while (i - count) >= 0 and (i + 1 + count) < string_len:
                if s[i - count] == s[i + 1 + count]:
                    count += 1
                else:
                    break
            if ( 2 * ( 1+count ) ) > longest_string_count:
                longest_string_count = ( 2 * ( 1 + count ) ) 
                longest_string = s[(i + 1 - count):(i + count + 1)]


        return longest_string
