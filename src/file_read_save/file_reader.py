def read_file(filepath) -> list:
    """
    The function reads the contents of the transferred file
    :param filepath: filepath of file with keywords
    :return: list of keywords
    """

    keywords = []
    with open(filepath, 'r') as f:
        for line in f:
            words = line.split(',')
            for word in words:
                keywords.append(word)

    return keywords
