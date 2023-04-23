import docker
from pathlib import Path
import os

docker_client = docker.from_env()


def docker_run_container(image: str,
                         detach: bool,
                         auto_remove: bool,
                         volumes: dict,
                         name: str):
    print(f'volume:\n{volumes}')

    my_container = docker_client.containers.run(image=image,
                                                detach=detach,
                                                auto_remove=auto_remove,
                                                volumes=volumes,
                                                name=name)
    # print(my_container, type(my_container))

    for line in my_container.logs(stream=True):
        print(line.decode("utf-8").strip())

    return my_container


def get_relative_path(file_name: str = 'config.yaml',
                      is_need_file_name: bool = True) -> str:
    current_dir = Path(os.path.dirname(os.path.abspath(__file__)))

    if is_need_file_name:
        abs_path = os.path.abspath(current_dir.joinpath('..', '..',
                                                        'tmp_config',
                                                        file_name))
    else:
        abs_path = os.path.abspath(current_dir.joinpath('..', '..',
                                                        'tmp_config'))
    relative_path_file = os.path.relpath(abs_path)
    return relative_path_file


def filling_file(my_text: str) -> None:
    """
    Заполняем файл
    :return:
    """
    relative_path_file = get_relative_path()

    with open(relative_path_file, 'w+') as file:
        file.write(my_text)


# filling_file(my_text='3333')

pyth_on_host = get_relative_path(is_need_file_name=False)
image = 'mms-image-python-test'
tag = '4.0'
fullName = image + ':' + tag
detach = True  # ключ -d
auto_remove = True  # ключ --rm
# entrypoint = '' or []
name = 'run_foo_v4'
# port = {'9000/tcp': '9000'}  # проброска портов

pyth_on_host = pyth_on_host.replace('\\', '/')
volumes = {r'C:\Users\m.merkulov\ExternalProjects\run_dcoker_container\tmp_config':
               {'bind': '/opt/cfg',
                'mode': 'ro'}}

docker_run_container(image=fullName,
                     detach=detach,
                     auto_remove=auto_remove,
                     volumes=volumes,
                     name=name)
