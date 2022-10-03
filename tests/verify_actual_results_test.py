import day1
import day1_pt2
import day2
import day2_pt2


def test_all():
    assert day1.run() == 1532
    assert day1_pt2.run() == 1571

    assert day2.run() == 1989014
    assert day2_pt2.run() == 2006917119
