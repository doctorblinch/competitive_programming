from time import time
from main import countAndSay #, countAndSay2

res_time = []

for _ in range(5):
    begin = time()
    res = countAndSay(50)

    time_took = time() - begin
    res_time.append(time_took)
    print(time_took, len(res))
