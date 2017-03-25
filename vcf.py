# coding=utf8
import csv
import quopri


def insert(name, number):
    f.write('BEGIN:VCARD\nVERSION:2.1\n')
    N2 = 'N;CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:;' + quopri.encodestring(
        name[0:3]) + ';' + quopri.encodestring(name[3:]) + ';;;\n'
    FN = 'FN;CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:' + quopri.encodestring(
        name) + '\n'
    TEL = 'TEL;CELL:' + number[0:1] + '-' + number[1:4] + '-' + number[
        4:7] + '-' + number[7:11] + '\n'
    f.write(N2)
    f.write(FN)
    f.write(TEL)
    f.write('END:VCARD\n')
    print name[0:1]


name = 1
phoneNumber = 9
f = open('data/test.vcf', 'a')
with open('data/numbers.csv') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        insert(row[name], row[phoneNumber])
