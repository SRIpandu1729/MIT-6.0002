from ps1a import *

__author__ = 'SRIpandu1729'


def test_ps1a_load_cows():
    cows = load_cows('ps1_cow_data.txt')
    assert cows['Maggie'] == 3
    assert cows['Herman'] == 7
    assert cows['Betsy'] == 9
    assert cows['Oreo'] == 6
    assert cows['Moo Moo'] == 3
    assert cows['Milkshake'] == 2
    assert cows['Millie'] == 5
    assert cows['Lola'] == 2
    assert cows['Florence'] == 2
    assert cows['Henrietta'] == 9


def test_ps1a_greedy_cow_transport():
    cows = greedy_cow_transport(load_cows('ps1_cow_data.txt'))
    print cows
    pass
