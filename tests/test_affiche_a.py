from src.fizzbuzz import affiche

def test_affiche_sans_parametre():
    out = affiche()
    assert out.startswith("12Fizz4BuzzFizz78FizzBuzz11Fizz1314FrisBee")
    assert out.endswith("FizzBuzz")
    assert len(out) > 0
