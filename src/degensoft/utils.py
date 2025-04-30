
def load_lines(filename: str) -> list:
    """
    :param filename: file path
    :return: list of all string except commented with # symbol
    """
    with open(filename) as f:
        return [row.strip() for row in f if row and not row.startswith('#')]