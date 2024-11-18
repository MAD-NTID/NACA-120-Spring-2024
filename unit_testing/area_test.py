import areas

def test_square_area():
    #setup
    sides = 8
    expected = 64

    #invoke
    actual = areas.square(sides)

    #analyze
    assert actual == expected

def test_rectangle_area():
    #setup
    width = 4
    height = 4
    expected = 16

    #invoke
    actual = areas.rectangle(width, height)

    #analyze
    assert actual == expected
