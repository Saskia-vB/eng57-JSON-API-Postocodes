# I want to make a get request to get more info on my postcode
# I need to check for my API documentation
# then build the target url with path and arguments
# then I need to use the package request to make the request
# I will receive a JSON that I need to parse into a dictionary

import requests

path ='http://api.postcodes.io/postcodes/'
arguments = 'ba17jx'

# Build url
url_target = path + arguments
print(url_target)

# make request and capture response (status code)
response = requests.get(url_target)
print(response)
print(type(response))

response_status_code = requests.get('https://api.postcodes.io/')
print(response_status_code.status_code)
if response_status_code.status_code == 400:
    print("oops something went wrong")
elif response_status_code.status_code == 200:
    print("great! successful")
else:
    print("Please try another time - better luck next time")


# Parsing or getting the dictionary out
print(response.json())
response_dictionary = response.json()

result_dictionary= response_dictionary['result']
print(result_dictionary)

for key in result_dictionary.keys():
    print(key, 'the value inside is', result_dictionary[key])