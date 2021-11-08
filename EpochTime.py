#!/usr/bin/env python3

import time

# get the current time 
current = int(time.time())

# add N minutes to the current time
print('Future Epoch time (in minutes)')
futureTime = input('>>> ')

future = int(time.time() + int(futureTime))

print('JWT format')
print('"iat": ' + str(current) + ',')
print('"exp": ' + str(future) + ',')
