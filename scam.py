# Please read the README.md before continuing.

import requests
import os
import random
import string
import json

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))

url = 'Enter the URL Here'

names = 'jason'

for name in names:
	name_extra = ''.join(random.choice(string.digits))

	username = 'jason' + name_extra + '@yahoo.com'
	password = ''.join(random.choice(chars) for i in range(8))

	requests.post(url, allow_redirects=False, data={
		'Enter the Log In string here': username,
		'Enter the Password string here': password
	})

	print('sending username %s and password %s' % (username, password))
