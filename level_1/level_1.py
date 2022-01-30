#!/usr/bin/python3
import requests

data_form = {'id':'3489','key':'','holdthedoor':'submit'}

for i in range(4096):
    requests.post("http://158.69.76.135/level1.php", data=data_form)

    print("vote:{}".format(i))
