import docker
from utils.utils_helper import get_relative_path

docker_client = docker.from_env()


def docker_build_image():
    docker_client.images.build(path='../../',  # path to Dockerfile
                               tag='mms-image-python-test_v2',
                               # name, tag=latest
                               rm=True,
                               labels={'name': 'mms-image-python-test_v2'}
                               )


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

    for line in my_container.logs(stream=True):
        print(line.decode("utf-8").strip())

    return my_container.short_id


def docker_get_list_container(all: bool = True, container_name: str = None):
    return docker_client.containers.list(all=all)


pyth_on_host = get_relative_path(is_need_file_name=False)
image = 'mms-image-python-test'
tag = '4.0'
fullName = image + ':' + tag
detach = True  # ключ -d
auto_remove = True  # ключ --rm
# entrypoint = '' or []
name = 'run_foo_v4'
# port = {'9000/tcp': '9000'}  # проброска портов

# volumes = {
#     r'../../tmp_config/config.yaml':
#     #    './config.yaml' :
#         {'bind': '/opt/cfg',
#          'mode': 'ro'}}
volumes = [r'C:\Users\m.merkulov\ExternalProjects\run_dcoker_container'
           r'\tmp_config\config.yaml:/opt/cfg/config.yaml']
