#!/usr/bin/env python
# Written by Rasmus Toftdahl Olesen <rto@pohldata.dk>
# Modified slightly by David A. Wheeler
# 202205 @zuksan adapt for python2, change color to github style
# Released under the GNU General Public License v. 2 or higher

from string import *
import sys

NAME = "sloc2html"
VERSION = "0.0.2"

# use sys.argv to attain argument of system.
# sys.argv[0] means the path of this code.
if len(sys.argv) != 2:
    print "Usage:"
    print "\t" + sys.argv[0] + " <sloc output file>"
    print "\nThe output of sloccount should be with --wide and --multiproject formatting"
    sys.exit()

# dict()
colors = {
    "python" : "blue",
    "ansic" : "#555555",
    "perl" : "purple",
    "cpp" : "#f34b7d",
    "sh" : "#89e051",
    "yacc" : "#4B6C4B",
    "lex" : "silver",
    "ruby" : "#701516",
    "cs" : "#178600",
    "java" : "brown",
    "ada" : "olive",
    "lisp" : "fuchsia",
    "objc" : "purple",
    "fortran" : "purple",
    "cobol" : "purple",
    "pascal" : "purple",
    "asm" : "purple",
    "csh" : "purple",
    "tcl" : "#e4cc98",
    "exp" : "purple",
    "awk" : "purple",
    "sed" : "purple",
    "makefile" : "#427819",
    "sql" : "purple",
    "php" : "purple",
    "modula3" : "purple",
    "ml" : "purple",
    "haskell" : "purple",
    "xml" : "orange",
    "javascript" : "#f1e05a"
    # Feel free to make more specific colors.
    }

print "<html>"
print "<head>"
print "<title>Counted Source Lines of Code (SLOC)</title>"
print "</head>"
print "<body>"
print "<h1>Counted Source Lines of Code</h1>"

# open result.txt
file = open ( sys.argv[1], "r" )

print "<h2>Projects</h2>"
line = ""
# read one line and move to next line until find out the string
while line != "SLOC\tDirectory\tSLOC-by-Language (Sorted)\n":
    line = file.readline()

print "<table>"
print "<tr><th>Lines</th><th>Project</th><th>Language distribution</th></tr>"
line = file.readline()
while line != "\n":
    lineSplitRes = line.split()
    line = file.readline()
    if len(lineSplitRes) < 3:
        continue
    (num, project, langs) = lineSplitRes
    print "<tr><td>" + num + "</td><td>" + project + "</td><td>"
    print "<table width=\"1000\"><tr>"
    for lang in split ( langs, "," ):
        if langs == '(none)' or lang =='(none)':
            break
        langLinePair = lang.split("=")
        if len(langLinePair) < 2:
            break
        l = langLinePair[0]
        n = langLinePair[1]
        print "<td bgcolor=\"" + colors[l] + "\" width=\"" + str( float(n) / float(num) * 1000 ) + "\">" + l + "=" + n + "&nbsp;(" + str(int(float(n) / float(num) * 100)) + "%)</td>"
    print "</tr></table>"
    print "</td></tr>"
print "</table>"

print "<h2>Languages</h2>"
while line != "Totals grouped by language (dominant language first):\n":
    line = file.readline()

print "<table>"
print "<tr><th>Language</th><th>Lines</th></tr>"
line = file.readline()
while line != "\n":
    lang, lines, per = split ( line )
    lang = lang[:-1]    # exclude the last character
    print "<tr><td bgcolor=\"" + colors[lang] + "\">" + lang + "</td><td>" + lines + " " + per + "</td></tr>"
    line = file.readline()
print "</table>"

print "<h2>Totals</h2>"
while line == "\n":
    line = file.readline()

print "<table>"
print "<tr><td>Total Physical Lines of Code (SLOC):</td><td>" + strip(split(line,"=")[1]) + "</td></tr>"
line = file.readline()
print "<tr><td>Estimated development effort:</td><td>" + strip(split(line,"=")[1]) + " person-years (person-months)</td></tr>"
line = file.readline()
line = file.readline()
print "<tr><td>Schedule estimate:</td><td>" + strip(split(line,"=")[1]) + " years (months)</td></tr>"
line = file.readline()
line = file.readline()
print "<tr><td>Total estimated cost to develop:</td><td>" + strip(split(line,"=")[1]) + "</td></tr>"
print "</table>"

file.close()

print "Please credit this data as \"generated using 'SLOCCount' by David A. Wheeler.\"\n"
print "</body>"
print "</html>"
