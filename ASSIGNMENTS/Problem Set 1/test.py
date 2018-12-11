from ps1a import *

__author__ = 'SRIpandu1729'


def test_ps1a():
    cows = load_cows('ps1_cow_data.txt')
    for keys, values in cows.items():
        print keys, values
