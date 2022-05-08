from collections import defaultdict
import unittest


def longest_substring_with_distinct_characters(string, k):
    win_start, max_len = 0, 0
    char_freqs = defaultdict(int)

    for win_end in range(len(string)):
        end_char = string[win_end]
        char_freqs[end_char] += 1

        while len(char_freqs) > sum(char_freqs.values()):
            right_char = string[win_start]
            char_freqs[right_char] -= 1
            if char_freqs[right_char] == 0:
                del char_freqs[right_char]
            win_start += 1

            max_len = max(max_len, win_end - win_start + 1)

            if win_start == win_end:
                break

    return max_len


class Test(unittest.TestCase):

    def test_sliding_window_1(self):
        string = 'araaci'
        k = 2
        result = longest_substring_with_distinct_characters(string, k)
        print('--', result)
        self.assertEqual(result, 4)


if __name__ == '__main__':
    unittest.main()
