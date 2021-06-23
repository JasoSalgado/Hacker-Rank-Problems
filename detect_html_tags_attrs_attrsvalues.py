"""
Sample Input

9
<head>
<title>HTML</title>
</head>
<object type="application/x-flash"
  data="your-file.swf"
  width="0" height="0">
  <!-- <param name="movie" value="your-file.swf" /> -->
  <param name="quality" value="high"/>
</object>
Sample Output

head
title
object
-> type > application/x-flash
-> data > your-file.swf
-> width > 0
-> height > 0
param
-> name > quality
-> value > high
Explanation

head tag: Print the head tag only because it has no attribute.

title tag: Print the title tag only because it has no attribute.

object tag: Print the object tag. In the next  lines, print the attributes type, data, width and                     height along with their respective values.

<!-- Comment --> tag: Don't detect anything inside it.

param tag: Print the param tag. In the next  lines, print the attributes name along with                     their respective values.
"""

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for at in attrs:
            print("-> {} > {}".format(at[0], at[1]))
    def handle_startendtag(self, tag, attrs):
        print(tag)
        for at in attrs:
            print("-> {} > {}".format(at[0], at[1]))

html = ""
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'

parser = MyHTMLParser()
parser.feed(html)
parser.close()
