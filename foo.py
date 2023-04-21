import time

lst = []
lst = ['England', 'Germany', 'Russia', 'China', 'Belgium']
for el in lst:
    print(f'{el} is country')

for _ in range(1000):
    time.sleep(1)
    print(f"I'm working {_} ...")