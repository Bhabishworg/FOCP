from sys import argv
from urllib.request import urlopen
from urllib.error import HTTPError, URLError

try:
    link = urlopen(argv[1])

except IndexError:
    print("No url Provided")
    
except HTTPError:
    print("HTTP error")

except URLError:
    print("It's not a working website")

else:
    print("It's a working website")
