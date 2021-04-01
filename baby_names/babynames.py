#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

import sys
import re
#from bs4 import BeautifulSoup
import codecs

"""Baby Names exercise
Define the extract_names() function below and change main()
to call it.
For writing regex, it's nice to include a copy of the target
text for inspiration.
Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...
Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""


def extract_names(filename):
    """
    Given a file name for baby.html, returns a list starting with the year string
    followed by the name-rank strings in alphabetical order.
    ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
    """
    # +++your code here+++
    """
    file = codecs.open(filename, "r", "utf-8")
    content = BeautifulSoup(file.read(),'lxml')
    table = content.find('h3')
    year = re.findall(r'\d+',str(table))
    
    baby_names = []
    baby_names.append(year[1])
    
    data = content.find_all('tr',align='right')
    """

    baby_names = []
    year = 0
    with open(filename,'r') as infile:
        data = infile.readlines()
    #print(data)
    for i in data:
        tag = "h3"
        names = r"<" + tag + " align=\"center\">(.*?)</" + tag + ">"
        table = re.findall(names,i)
        if table:
            year = re.findall(r'\d+', str(table))
            #print(year)
            break

    baby_names.append(year[0])
    for i in data:
        tag = "td"
        names = r"<" + tag + ">(.*?)</" + tag + ">"
        name_l = re.findall(names, i)
        if name_l:
            baby_names.append(name_l[1]+' '+name_l[0])
            baby_names.append(name_l[2] + ' ' + name_l[0])
    print(baby_names[0])
    print()
    print()
    #for i in sorted(baby_names[1:]):
        #print(i)

    return baby_names


def main():
    # This command-line parsing code is provided.
    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]

    if not args:
        print('usage: [--summaryfile] file [file ...]')
        sys.exit(1)

    # Notice the summary flag and remove it from args if it is present.
    summary = False
    if args[0] == '--summaryfile':
        summary = True
        del args[0]
    f = sys.argv[2]
    file = open("summaryfile.txt","w+")

    b = extract_names(f)
    # +++your code here+++
    # For each filename, get the names, then either print the text output
    # or write it to a summary file
    file.write(b[0])
    file.write("\n\n")
    for i in sorted(b[1:]):
        file.write(i)
        file.write("\n")

if __name__ == '__main__':
    main()