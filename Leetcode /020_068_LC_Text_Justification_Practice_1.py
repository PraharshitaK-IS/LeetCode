#https://leetcode.com/problems/text-justification/?envType=study-plan-v2&envId=top-interview-150
# This one was a toughie
#Didn't properly comprehend how it does it greedily 
#Need to come Back!!!


class Solution:
    def fullJustify(self, words, maxWidth):
        result = []
        i = 0
        n = len(words)

        while i < n:
            line_len = len(words[i])
            j = i + 1
            while j < n and line_len + len(words[j]) + (j - i) <= maxWidth:
                line_len += len(words[j])
                j += 1

            num_words = j - i
            num_spaces = maxWidth - line_len
            line = ""

            if j == n or num_words == 1:
                line = ' '.join(words[i:j])
                line += ' ' * (maxWidth - len(line))
            else:
                spaces_between_words = num_spaces // (num_words - 1)
                extra_spaces = num_spaces % (num_words - 1)

                for k in range(i, j - 1):
                    line += words[k]
                    line += ' ' * (spaces_between_words + (1 if k - i < extra_spaces else 0))
                line += words[j - 1]

            result.append(line)
            i = j

        return result
