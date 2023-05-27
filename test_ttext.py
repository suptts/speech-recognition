from app import ttext


def test_ttext():
    assert "สวัสดีชาวโลก" in ttext("Hello World")
