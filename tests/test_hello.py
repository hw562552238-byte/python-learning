from python_learning.hello import hello

def test_hello(capsys):
    hello()
    assert "Hello from python_learning!" in capsys.readouterr().out
