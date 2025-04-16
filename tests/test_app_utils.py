from app.utils import get_response
def test_get_response():
    assert get_response("Hello") == "Response for: Hello"
    assert get_response("What's the weather like?") == "Response for: What's the weather like?"