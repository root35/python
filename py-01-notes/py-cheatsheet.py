tokens = re.split('\s+', parag_no_punct.lower())
# better than str.split = split based on pattern

str_nums = ["4", "8", "6", "5", "3", "2", "8", "9", "2", "5"]
int_nums = list(map(int, str_nums))

from collections import deque
s = deque()
s.append("eat")
s.append("sleep")
s.append("code")
s.pop()
> 'code'
s.count('code')
> 2


h = []
heappush(h, (5, 'write code'))
heappush(h, (7, 'release product'))
heappush(h, (1, 'write spec'))
heappop(h)
> (1, 'write spec')


from heapq import *

class Meeting:
      def __init__(self, start, end):
        self.start = start
        self.end = end

      def __lt__(self, other):
        ''' Used to sort meetings in heapq based on ending hour. '''
        return self.end < other.end
