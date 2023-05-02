import time


def read_file() -> None:
    with open('/opt/cfg/config.yaml', 'r') as file:
        for line in file:
            print(line.rstrip('\n'))

lst = []
lst = ['England', 'Germany', 'Russia', 'China', 'Belgium']
for el in lst:
    print(f'{el} is country')

print(f'Start read file /opt/cfg/config.yaml')
read_file()
print(f'End read file /opt/cfg/config.yaml')

for _ in range(10):
    time.sleep(1)
    print(f"I'm working {_} ...")
