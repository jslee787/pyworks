f = open("c:/web_dev/pyfile/number.txt", 'w')
f.write('%d\n' %45)
f.write('%.2f\n' %12.34)
f.write('%d\n' %(45 + 1))

i = 3
j = 4
times = '%d x %d = %d' % (i, j, i*j)
f.write(times)

f.close()