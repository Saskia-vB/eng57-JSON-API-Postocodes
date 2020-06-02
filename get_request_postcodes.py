# 1st we need a way to talk HTTP

## we'll use the requests package that is very stable and widely used

# this is a standard py library no need to install
# import time
#
# time.sleep(1)

# requests is not a standard library and must be installed with a package manager
    # package: is an external library of code, not native to python (or vanilla python)
    # a package manager: install and manages this package

# python, ruby, javascript, java, C# almost all modern

import requests

# I want to make a get request to get more info on my postcode
# I need to check for my API documentation
# then build the target url with path and arguments
# then I need to use the package request to make the request
# I will receive a JSON that I need to parse into a dictionary

path = 'http://api.postcodes.io/postcodes/'
arguments = 'e147le'

# Build url
url_target= path + arguments
print(url_target)

# Make request and capture response
response = requests.get(url_target)
print(response)
print(type(response))

# Parsing or getting the dictrionary out
print(response.json())
response_dictionary = response.json()

print(type(response_dictionary))

# for key in response_dictionary.keys():
#     print(key)

result_dictionary = response_dictionary['result']
print(result_dictionary)

for key in result_dictionary.keys():
    print(key, 'the value inside is', result_dictionary[key])