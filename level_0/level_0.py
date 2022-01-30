#!/usr/bin/python3
import requests

data_form = {'id':'3489','holdthedoor':'submit'}

for i in range(1024):
    requests.post("http://158.69.76.135/level0.php", data=data_form)

    print("vote:{}".format(i))
