import Lab2.bmi as bmi

def test_bmi_normal_weight():
    result = bmi.calculate_bmi(1.75,60)
    assert (result == 0)

def test_bmi_over_weight():
    result = bmi.calculate_bmi(1.00,100)
    assert (result == 1)
def test_bmi_under_weight():
    result = bmi.calculate_bmi(1.75, 53)
    assert (result == -1)