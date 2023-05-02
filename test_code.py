import docker
import os
from pathlib import Path

docker_client = docker.from_env()

########################## BUILD IMAGE START ###############################
dockerfile_path = '../../'
rm = True
tag = '1.0'
labes = {'name': 'mms1'}


def docker_build_image(path: str, tag: str, labals: dict, rm: bool):
    my_image = docker_client.images.build(path=path,
                                          tag=tag,
                                          labels=labals,
                                          rm=rm)

    print(my_image, type(my_image))


########################## BUILD IMAGE END ###############################

########################## RUN container START ################################
image = 'mms-image-python-test'
tag = '2.0'
fullName = image + ':' + tag
detach = True  # ключ -d
auto_remove = True  # ключ --rm
# entrypoint = '' or []
name = 'run_foo_v2'
# port = {'9000/tcp': '9000'}  # проброска портов
volumes = {'путь/на/хсоте': {'bind': '/opt/cfg/application.yaml', 'mode': 'ro'}}


def docker_run_container(image: str,
                         detach: bool,
                         auto_remove: bool,
                         name: str):
    my_container = docker_client.containers.run(image=image,
                                                detach=detach,
                                                auto_remove=auto_remove,
                                                name=name)
    print(my_container, type(my_container))

    for line in my_container.logs(stream=True):
        print(line.decode("utf-8").strip())

    return my_container


# docker_run_container(image=fullName, detach=detach, auto_remove=auto_remove,
#                      name=name)

########################## RUN container END ###############################

########################## GET CONTAINER START ###############################
container_name = 'run_foo'
filter = {'name': container_name}


def docker_get_container_id(filter: dict):
    my_containers = docker_client.containers.list(all=True,
                                                  filters=filter)
    # print(my_container, type(my_container))
    for container in my_containers:
        print(container, type(container), container.id, container.short_id)

    return my_containers[0]


########################## GET CONTAINER END ###############################


######################## CREATE CONTAINER START###############################

# def docker_create_container():
# image = 'mms-image-python-test:2.0'
# docker_client.containers.create()
######################## CREATE CONTAINER END###############################


def read_file() -> None:
    with open('src/docker/config.yaml', 'r') as file:
        for line in file:
            print(line.rstrip('\n'))


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


#
# print(get_relative_path())

d = {'a', 123}
