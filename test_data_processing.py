from data_processing import fill_missing, remove_duplicates, scale_0_to_1
 
 
def test_remove_duplicates():
    assert remove_duplicates([1, 2, 2, 3, 1]) == [1, 2, 3]
 
 
def test_fill_missing():
    assert fill_missing([10, None, 30]) == [10, 20.0, 30]
 
 
def test_scale_gives_0_to_1():
    result = scale_0_to_1([5, 10, 15])
    assert min(result) == 0.0
    assert max(result) == 1.0
 
 
def test_scale_examples():
    # Many test cases in one test: (input, expected answer)
    cases = [
        ([0, 5, 10], [0.0, 0.5, 1.0]),
        ([10, 20], [0.0, 1.0]),
        ([-5, 0, 5], [0.0, 0.5, 1.0]),
    ]
    for values, expected in cases:
        assert scale_0_to_1(values) == expected
 
 
def test_scale_with_all_equal_values():
    assert scale_0_to_1([7, 7, 7]) == [0.0, 0.0, 0.0]
