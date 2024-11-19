from .processing import process

def test_process() -> None:
    result = process()
    assert isinstance(result, str)
    assert result.startswith('This')