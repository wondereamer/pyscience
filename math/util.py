import bisect


def trim(t, p=0.01):
    """Trims the largest and smallest elements of t.

    Args:
        t: sequence of numbers
        p: fraction of values to trim off each end

    Returns:
        sequence of values
    """
    t.sort()
    n = int(p * len(t))
    t = t[n:-n]
    return t



def binom(n, k, d={}):
    """Compute the binomial coefficient "n choose k".

    Args:
      n: number of trials
      k: number of successes
      d: map from (n,k) tuples to cached results

    Returns:
      int
    """
    if k == 0:
        return 1
    if n == 0:
        return 0

    try:
        return d[n, k]
    except KeyError:
        res = binom(n-1, k) + binom(n-1, k-1)
        d[n, k] = res
        return res


class interpolator(object):
    """Represents a mapping between sorted sequences; performs linear interp.

    Attributes:
        xs: sorted list
        ys: sorted list
    """
    def __init__(self, xs, ys):
        self.xs = xs
        self.ys = ys

    def lookup(self, x):
        """Looks up x and returns the corresponding value of y."""
        return self._bisect(x, self.xs, self.ys)

    def reverse(self, y):
        """Looks up y and returns the corresponding value of x."""
        return self._bisect(y, self.ys, self.xs)

    def _bisect(self, x, xs, ys):
        """Helper function."""
        if x <= xs[0]:
            return ys[0]
        if x >= xs[-1]:
            return ys[-1]
        i = bisect.bisect(xs, x)
        frac = 1.0 * (x - xs[i-1]) / (xs[i] - xs[i-1])
        y = ys[i-1] + frac * 1.0 * (ys[i] - ys[i-1])
        return y


