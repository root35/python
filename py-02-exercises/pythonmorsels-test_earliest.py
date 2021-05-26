import unittest


# from earliest import get_earliest


def get_earliest(*dates):
    def format_date(date): return (date[2], *date[:2])
    d = [tuple(format_date(l.split('/'))) for l in dates]
    earliest = d.index(min(d))
    return dates[earliest]


# !!!
# Trey's solution: tuples (same as me but coded differently)
def get_earliest(*dates):
    """Return earliest of given MM/DD/YYYY-formatted date strings."""
    def date_key(date):
        (m, d, y) = date.split('/')
        return (y, m, d)
    return min(dates, key=date_key)


# Trey's solution: regexps
def get_earliest(date1, date2):
    """Return earliest of two MM/DD/YYYY-formatted date strings."""
    DATE_RE = re.compile(r'^(\d{2})/(\d{2})/(\d{4})$')
    (m1, d1, y1) = DATE_RE.search(date1).groups()
    (m2, d2, y2) = DATE_RE.search(date2).groups()
    return date1 if (y1, m1, d1) < (y2, m2, d2) else date2


# Trey's solution: datetime
from datetime import datetime
def get_earliest(string1, string2):
    """Return earliest of two MM/DD/YYYY-formatted date strings."""
    date1 = datetime.strptime(string1, "%m/%d/%Y")
    date2 = datetime.strptime(string2, "%m/%d/%Y")
    if date1 < date2:
        return string1
    else:
        return string2


class GetEarliestTests(unittest.TestCase):

    """Tests for get_earliest."""

    def test_same_month_and_day(self):
        newer = "01/27/1832"
        older = "01/27/1756"
        self.assertEqual(get_earliest(newer, older), older)

    def test_february_29th(self):
        newer = "02/29/1972"
        older = "12/21/1946"
        self.assertEqual(get_earliest(newer, older), older)

    def test_smaller_month_bigger_day(self):
        newer = "03/21/1946"
        older = "02/24/1946"
        self.assertEqual(get_earliest(older, newer), older)

    def test_same_month_and_year(self):
        newer = "06/24/1958"
        older = "06/21/1958"
        self.assertEqual(get_earliest(older, newer), older)

    def test_invalid_date_allowed(self):
        newer = "02/29/2006"
        older = "02/28/2006"
        self.assertEqual(get_earliest(older, newer), older)

    def test_two_invalid_dates(self):
        newer = "02/30/2006"
        older = "02/29/2006"
        self.assertEqual(get_earliest(newer, older), older)

    def test_invalid_date_with_earlier_month_but_more_days(self):
        newer = "02/01/0000"
        older = "01/99/0000"
        self.assertEqual(get_earliest(newer, older), older)

    # To test the Bonus part of this exercise, comment out the following line
    @unittest.expectedFailure
    def test_many_dates(self):
        d1 = "01/24/2007"
        d2 = "01/21/2008"
        d3 = "02/29/2009"
        d4 = "02/30/2006"
        d5 = "02/28/2006"
        d6 = "02/29/2006"
        self.assertEqual(get_earliest(d1, d2, d3), d1)
        self.assertEqual(get_earliest(d1, d2, d3, d4), d4)
        self.assertEqual(get_earliest(d1, d2, d3, d4, d5, d6), d5)


if __name__ == "__main__":
    unittest.main(verbosity=2)
