import docker

# IMAGE = 'mms-img-python:1.0'

docker_client = docker.from_env()
list_images = docker_client.images.list()
for image in list_images:
    if len(image.tags) != 0:
        print(image)
        print(f'id => {image.id}')
        print(f'label => {image.labels}', type(image.labels))
        print(f'tags => {image.tags}')
        print('*' * 16)

list_containers = docker_client.containers.list()

#### CREATE!!!
my_container = docker_client.containers.create(image='mms-img-python:1.0',
                                               command='--rm',
                                               name='mms_container_1')

print(my_container)

my_container.start()

# image = 'mms-img-python:1.0'
# container_name = 'mms_container'
# #### RUN!!!!!!!!!
# container = docker_client.containers.run(image=image,
#
#                                          detach=True)
# print(container, type(container))

# for line in container.logs(stream=True):
#     print(line.decode("utf-8").strip())

# def run_docker_container(image: str,
#                          is_remove: bool = True,
#                          is_detach: bool = True) -> None:
#     docker_client.containers.run(image=image,
#                                  remove=is_remove,
#                                  detach=is_detach)
