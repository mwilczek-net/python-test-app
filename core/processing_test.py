from .processing import process, number_list

def test_process() -> None:
    result = process()
    assert isinstance(result, str)
    assert result.startswith('This')

def test_number_list() -> None:
    assert number_list() == [-0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]