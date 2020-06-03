# Next Job:
#

# Make it functional:
# Make a function that take in a post code:

import requests

path ='http://api.postcodes.io/postcodes/'
arguments = 'ba17jx'

# Build url
url_target = path + arguments
print(url_target)

# Handle your errors

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

# for all the status codes responds back
# with your longitude is <>,
# your latitude is <>
# and your parliamentary_constituenc <>,
# your nuts value is

response_dictionary = response.json()

result_dictionary = response_dictionary['result']
longitude = result_dictionary['longitude']
print("your longitude is ", longitude)
latitude = result_dictionary['latitude']
print("your latitude is ", latitude)
parliamentary_constituency = result_dictionary['parliamentary_constituency']
print("your parliamentary constituency is ", parliamentary_constituency)
nuts = result_dictionary['nuts']
print("your nuts value is ", nuts)

# make it into a program
# as a user I should be prompted for a post code and I should get back the long, lat, parliament_constituency, and the NUTS value
while True:
    user_input = input("Please enter your postcode:")
    user_url_target = path + user_input
    print(user_url_target)
    user_response = requests.get(user_url_target)
    user_response_dictionary = user_response.json()
    user_result_dictionary = user_response_dictionary['result']
    longitude = user_result_dictionary['longitude']
    print("your longitude is ", longitude)
    latitude = user_result_dictionary['latitude']
    print("your latitude is ", latitude)
    parliamentary_constituency = user_result_dictionary['parliamentary_constituency']
    print("your parliamentary constituency is ", parliamentary_constituency)
    nuts = user_result_dictionary['nuts']
    print("your nuts value is ", nuts)
    if user_input == "Thank you, I am done for today":
        break

# as a user I should keep being prompted for input until I say: "Thank you, I am done for today" or I use the word 'exit' in any string

# Make it follow:
# - DRY
# - Separation of concerns
