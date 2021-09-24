#!/usr/bin/env python3
import cgi, cgitb, sys, os, time
from templates import login_page
from templates import secret_page
from http import cookies
import secret


form =  cgi.FieldStorage()

username = form.getvalue("username")
password = form.getvalue("password")

print(login_page())

print("<html>")
print("<head>")
print("<title>Hello - Second CGI Program</title>")
print("</head>")
print("<body>")
print("<p><b>Username</b> %s <b>password</b> %s </p>" % (username, password))
print("</body>")
print("</html>")




if secret.username == username and secret.password == password :
	cookie = cookies.SimpleCookie()
	cookie['lastvisit'] = str(time.time())
	cookie['UserID'] = username
	cookie['Password'] = password
	print(cookie)
	print('<html><body>')
	print('<p>')
	print('server time is', time.asctime(time.localtime()))
	print('</p>')
	print('</body></html>')

	cookie_string = os.environ.get('HTTP_COOKIE')

	cookie.load(cookie_string)
	lastvisit = float(cookie['lastvisit'].value)
	print('<p>Your last visit was at')
	print(time.asctime(time.localtime(lastvisit)), '</p>')
	print('</body></html>')

	print(secret_page(cookie['UserID'].value, cookie['Password'].value))



