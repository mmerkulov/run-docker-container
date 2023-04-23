import time


time.sleep(120)
def read_file() -> None:
    with open('/opt/cfg/application.yaml', 'r') as file:
        for line in file:
            print(line.rstrip('\n'))


lst = []
lst = ['England', 'Germany', 'Russia', 'China', 'Belgium']
for el in lst:
    print(f'{el} is country')

print(f'Start read file /opt/cfg/application.yaml\n')
read_file()
print(f'\nEnd read file /opt/cfg/application.yaml')

for _ in range(10):
    time.sleep(1)
    print(f"I'm working {_} ...")