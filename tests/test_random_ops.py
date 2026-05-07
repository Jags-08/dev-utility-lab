from dev_utils.random_ops import random_int, random_choice, shuffle_list, generate_password

def test_random_int():
    val = random_int(1, 10)
    assert 1 <= val <= 10

def test_random_choice():
    val = random_choice([1, 2, 3])
    assert val in [1, 2, 3]

def test_shuffle_list():
    lst = [1, 2, 3, 4, 5]
    res = shuffle_list(lst.copy())
    assert set(lst) == set(res)

def test_generate_password():
    pwd = generate_password(16)
    assert len(pwd) == 16
