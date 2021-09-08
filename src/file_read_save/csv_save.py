from pathlib import Path


def csv_save_links(file: str, content: list):
    """
    Function saves gathered contents in passed file
    :param content: list of gathered links
    :param file: file path to proper file
    :return: None
    """
    filepath = get_filepath(file)
    with open(filepath, 'w') as f:
        for c in content:
            f.write('{}\n'.format(c))


def csv_save_results_nr(file: str, content: dict):
    """
    Function for saving downloaded search results numbers
    """
    filepath = get_filepath(file)
    with open(filepath, 'w') as f:
        for c in content:
            f.write('{},{}\n'.format(c, content.get(c)))


def get_filepath(file: str):
    files_fd = Path('files/')
    filepath = files_fd / file

    return filepath
