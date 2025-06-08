import time

import requests
nbrRequest=25

for i in range(nbrRequest):
    start = time.time()
    x = requests.get('http://127.0.0.1:5000/factorial?no=150000')
    end = time.time()
    print(i, end - start)

print(x.text)
