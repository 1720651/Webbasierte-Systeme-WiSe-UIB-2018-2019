#!python
# -*- encoding: utf-8 -*-
import cgi
print ("Content-type: text/html")
print()
print("<!DOCTYPE HTML>")
print ("<html><head>")
print ("<meta charset='UTF-8'/>")
print ("<title>Begrüßung</title>")
print ("</head><body>")
form = cgi.FieldStorage()
vorname = form.getvalue('vorname')
nachname = form.getvalue('nachname')
print ("<p>Hallo", vorname,