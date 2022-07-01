# Write a function bunny that accepts an integer parameter count. count represents a number of bunnies and each bunny has two big floppy ears. We want to compute the total number of ears across all the bunnies recursively (without loops or multiplication).

# Here are the tests:
def bunny(count):
    if count == 0:
        return 0
    return bunny(count -1) +2


def test_bunny_zero_bunnies():
    assert bunny(0) == 0


def test_bunny_one_bunny_has_two_ears():
    assert bunny(1) == 2


def test_bunny_fifty_bunnies_have_100_ears():
    assert bunny(50) == 100