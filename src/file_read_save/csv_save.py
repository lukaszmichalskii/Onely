from pathlib import Path


def csv_save_links(file: str, content: list) -> None:
    """
    Function saves gathered contents in passed file
    :param: file: file to save
    :param: content: content to save
    """
    filepath = get_filepath(file)
    with open(filepath, 'w') as f:
        for c in content:
            f.write('{}\n'.format(c))


def csv_save_results_nr(file: str, content: dict) -> None:
    """
    Function for saving downloaded search results numbers
    :param: file: file to save
    :param: content: content to save
    """
    filepath = get_filepath(file)
    with open(filepath, 'w') as f:
        for c in content:
            f.write('{},{}\n'.format(c, content.get(c)))


def get_filepath(file: str) -> Path:
    """
    Function provide complete path to passed file name
    :param: file: file name of file we want to get path
    :return: filepath: complete file path to passed file
    """
    files_fd = Path('files/')
    filepath = files_fd / file

    return filepath
