import os.path

from src.docker.DockerClient import docker_run_container
from src.docker.DockerClient import docker_get_list_container
from utils.utils_helper import write_to_file
from utils.utils_helper import get_relative_path


########################################################################
print(f'step #1')
image = 'mms-image-python-test'
tag = '4.0'
fullName = image + ':' + tag
detach = True  # ключ -d
auto_remove = True  # ключ --rm
name = 'run_foo_v4'
path = get_relative_path(is_need_file_name=False)
volumes = {
    path:
        {'bind': '/opt/cfg',
         'mode': 'ro'}}
#
# print(f'volumes => {volumes}')

# volumes = [r'C:\Users\m.merkulov\ExternalProjects\run_dcoker_container'
#            r'\tmp_config\config.yaml:/opt/cfg/config.yaml']

running_container = docker_run_container(image=fullName,
                                         detach=detach,
                                         auto_remove=auto_remove,
                                         volumes=volumes,
                                         name=name)

########################################################################
cur_path = get_relative_path()
print(f'step #2')
text = '1\n2\n3'
write_to_file(cur_path=cur_path, text=text)
########################################################################
print(f'step #3')
is_running = True
while is_running:
    list_conainers = docker_get_list_container(all=True)
    print(f'waiting ...')
    if is_running not in list_conainers:
        is_running = False
########################################################################
print(f'step #4')
docker_run_container(image=fullName,
                     detach=detach,
                     auto_remove=auto_remove,
                     volumes=volumes,
                     name=name)
