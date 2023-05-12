"""Module with functions."""


def largest_sum(numbers: list[int]) -> tuple[int, int]:
    """Encontra e retorna os dois números que somados dão o maior valor."""
    if len(numbers) < 2:
        return None
    segundo = max(numbers)
    numbers.remove(segundo)
    primeiro = max(numbers)

    return primeiro, segundo
