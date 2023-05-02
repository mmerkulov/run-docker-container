import os
from pathlib import Path


def write_to_file(cur_path: str, text: str):
    with open(cur_path, 'w+') as file:
        file.write(text)


def get_relative_path(file_name: str = 'config.yaml',
                      is_need_file_name: bool = True) -> str:
    current_dir = Path(os.path.dirname(os.path.abspath(__file__)))

    if is_need_file_name:
        abs_path = os.path.abspath(current_dir.joinpath('..',
                                                        'tmp_config',
                                                        file_name))
    else:
        abs_path = os.path.abspath(current_dir.joinpath('..',
                                                        'tmp_config'))
    # relative_path_file = os.path.relpath(abs_path)
    relative_path_file = abs_path
    return relative_path_file


def filling_file(my_text: str) -> None:
    """
    Заполняем файл
    :return:
    """
    relative_path_file = get_relative_path()

    with open(relative_path_file, 'w+') as file:
        file.write(my_text)
