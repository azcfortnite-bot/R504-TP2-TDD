def _mot(n: int) -> str:
    if n % 15 == 0:
        return "FrisBee"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)

def affiche() -> str:
    return "".join(_mot(n) for n in range(1, 101))
