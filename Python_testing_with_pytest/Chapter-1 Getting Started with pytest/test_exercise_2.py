def test_passing():
    number_list = [1, 2, 4, 5]
    a = 1
    b = 4
    assert 3 in number_list
    assert a < b
    assert 'fizz' not in 'fizzbuzz'
    assert 'xyz' in 'abcwxcyz'
