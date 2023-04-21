import docker

# IMAGE = 'mms-img-python:1.0'

docker_client = docker.from_env()

dockerfile_path = '../../'
rm = True
tag = '1.0'
labes = {'name': 'mms1'}


### BUILD
def docker_build_image(path: str, tag: str, labals: dict, rm: bool):
    my_image = docker_client.images.build(path=path,
                                          tag=tag,
                                          labels=labals,
                                          rm=rm)

    print(my_image, type(my_image))
    # (<Image: ''>, <itertools._tee object at 0x0000013D4F7A68C0>) <class 'tuple'>


#### RUN container
image = 'mms-img-python'
tag = '1.0'
fullName = image + ':' + tag
detach = True  # ключ -d
entrypoint = '' or []
name = 'run_foo'
port = {'9000/tcp': '9000'}  # проброска портов
volumes = {'путь/на/хсоте': {'bind': 'куда/пробросить', 'mode': 'ro'}}


def docker_run_container(image: str, detach: bool, name: str):
    my_container = docker_client.containers.run(image=fullName,
                                                detach=detach,
                                                name=name
                                                )
    print(my_container, type(my_container))

    for line in my_container.logs(stream=True):
        print(line.decode("utf-8").strip())

    return my_container


# GET CONTAINER
container_name = 'run_foo'
filter = {'name': container_name}


def docker_get_container_id(filter: dict):
    my_containers = docker_client.containers.list(all=True,
                                                  filters=filter)
    # print(my_container, type(my_container))
    for container in my_containers:
        print(container, type(container), container.id, container.short_id)

    return my_containers[0]


# ec41b02e8427
# docker_client.containers.start()

c = docker_get_container_id(filter)
print(c, type(c))
# c.start()
r = c.logs(stream=True)
print(r, type(r))
for q in c.logs(stream=True):
    print(q.decode("utf-8").strip())

# list_images = docker_client.images.list()
# for image in list_images:
#     if len(image.tags) != 0:
#         print(image)
#         print(f'id => {image.id}')
#         print(f'label => {image.labels}', type(image.labels))
#         print(f'tags => {image.tags}')
#         print('*' * 16)
#
# list_containers = docker_client.containers.list()
#
# #### CREATE!!!
# my_container = docker_client.containers.create(image='mms-img-python:1.0',
#                                                command='--rm',
#                                                name='mms_container_1')
#
# print(my_container)
#
# my_container.start()
#
# # image = 'mms-img-python:1.0'
# # container_name = 'mms_container'
# # #### RUN!!!!!!!!!
# # container = docker_client.containers.run(image=image,
# #
# #                                          detach=True)
# # print(container, type(container))
#
# # for line in container.logs(stream=True):
# #     print(line.decode("utf-8").strip())
#
# # def run_docker_container(image: str,
# #                          is_remove: bool = True,
# #                          is_detach: bool = True) -> None:
# #     docker_client.containers.run(image=image,
# #                                  remove=is_remove,
# #                                  detach=is_detach)
