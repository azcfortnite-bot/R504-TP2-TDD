def _mot(n: int) -> str:
    if n % 15 == 0:
        return "FrisBee"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)


def affiche(n1=None, n2=None) -> str:
    """
    Comportements :
    - affiche()        -> 1..100
    - affiche(n)       -> 1..n
    - affiche(n1, n2)  -> n1..n2 (inclusif)
    """
    if n1 is None and n2 is None:
        start, stop = 1, 100
    elif n2 is None:
        start, stop = 1, n1
    else:
        start, stop = n1, n2
    return "".join(_mot(i) for i in range(start, stop + 1))
