# Simple script for get news from fc.put.poznan.pl

# -*- coding: utf-8 -*-
import urllib.request
import time

u2 = urllib.request.urlopen('http://fc.put.poznan.pl/informacje-dla-studentow/student-w%2C79.html')

def main():
    c = 1
    pushed = False
    i = 100000
    lst = []
    dyn_lst = []
    for lines in u2.readlines():
        if "left_news" in str(lines):
            i = c * 1
        if c > i:
            lines = lines.decode('utf-8')
            dyn_lst = str(lines).split(">")

        for j in dyn_lst:
            if pushed:
                j = j.replace("</div","")
                j = j.replace("/", " ")
                if len(j) != 0:
                    if "2018" in j:
                        lst.append("")
                    lst.append(j)
                pushed = False
            if "news-date" in j or "news-title" in j or "<div class=\"field-content\"" in j:
                pushed = True
        c += 1

    for lin in lst:
        print (lin)
    time.sleep(3)
if __name__ == '__main__':
    main()
