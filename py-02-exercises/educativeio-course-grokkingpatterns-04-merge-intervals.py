import unittest


from __future__ import print_function

class Interval:
  def __init__(self, start, end):
    self.start = start
    self.end = end

  def print_interval(self):
    print("[" + str(self.start) + ", " + str(self.end) + "]", end='')

  def overlaps(self, interval):
    '''
    Since input intervals are sorted, the condition for overlap is: b.start <= a.end
    '''
    return interval.start <= self.end

  def merge(self, interval):
    ''' Input intervals are sorted on start index. '''
    new_interval = Interval(self.start, max(self.end, interval.end))
    return new_interval



def merge(intervals):
  if len(intervals) < 2:
    return intervals

  # Sort the intervals on start time
  intervals.sort(key=lambda x: x.start)

  # Merge the consecutive overlapping intervals.
  merged = []
  new_interval = intervals[0]

  for i in range(1, len(intervals)):
    current_interval = intervals[i]
    if new_interval.overlaps(current_interval):
      new_interval = new_interval.merge(current_interval)
    else:
      merged.append(new_interval)
      new_interval = current_interval

  merged.append(new_interval)

  return merged
