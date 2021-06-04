def _check_length(word):
    return len(word) > 10

def test_passing():
    # below will print with pytest option -s
    print('In method <test_passing>.')
    word = "Kristopher Bucyk"
    assert _check_length(word)

def test_another_failing():
    word = "kris"
    assert _check_length(word)
