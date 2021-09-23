#!/usr/bin/env python3

import os
import json

print("Content-Type:text/html\r\n\r\n")
print("<title>Test CGI</title>")
print("<p>Hello World cmput404 class!</p>")
 
# printing environment variables
environDict = dict(os.environ)
environJson = json.dumps(environDict, indent = 4)
print(environJson)

print("<p>Report the values of query parameters:</p>")
print("\"QUERY_STRING\": "  + "\"" + environDict["QUERY_STRING"] + "\"")

print("<p>Report the user's browser:</p>")
print("\"HTTP_USER_AGENT\": "  + "\"" + environDict["HTTP_USER_AGENT"] + "\"")