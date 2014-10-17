# -*- coding: utf-8 -*-

from bisect import bisect_left


def take_closest(source_list, number):
    """
    Assumes source_list is sorted. Returns closest value to given number.

    If two numbers are equally close, return the smallest number.
    It's about 20 times faster than with_min one

    :param list source_list: sorted source list
    :param number: number for search
    :type number: float, int
    :rtype: tuple of (int|float, int)
    :return: value, position

    >>> source = [0, 1, 2, 3, 4, 5.55, 5.65, 5.7, 6, 6.1]
    >>> #: position would be closest to 5.55 as it greater than 4 and lesser
    >>> #: than 5.55
    >>> take_closest(source, 5.53)
    (5.55, 5)
    >>> #: position would be closest to 5.65 as it greater than 5.55
    >>> take_closest(source, 5.56)
    (5.55, 6)
    >>> take_closest(source, 5.60)
    (5.55, 6)
    >>> take_closest(source, 5.63)
    (5.65, 6)
    >>> take_closest([], 123)
    (-1, 0)
    """
    if len(source_list) <= 0:
        return -1, 0
    pos = bisect_left(source_list, number)
    if pos == 0:
        return source_list[0], pos
    if pos == len(source_list):
        return source_list[-1], pos
    before = source_list[pos - 1]
    after = source_list[pos]
    if after - number < number - before:
        return after, pos
    return before, pos


def with_min(source_list, number):
    return min(source_list, key=lambda x: abs(x - number))

