import day1
import day1_pt2
import day2
import day2_pt2
import day3
import day3_pt2
import day4
import day4_pt2


def test_all():
    assert day1.run() == 1532
    assert day1_pt2.run() == 1571

    assert day2.run() == 1989014
    assert day2_pt2.run() == 2006917119

    assert day3.run() == 1082324
    assert day3_pt2.run() == 1353024

    assert day4.run() == 58374
    assert day4_pt2.run() == 11377
