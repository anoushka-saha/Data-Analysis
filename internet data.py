# Anoushka Saha
# Fetching Internet Data
# Python for Data Analysis
# July 13th, 2024

# Importing necessary modules
import urllib.request

# Opening URL and reading data
weburl = urllib.request.urlopen("http://google.com")
print("Result code: ", weburl.getcode())
data = weburl.read()
print(data)

