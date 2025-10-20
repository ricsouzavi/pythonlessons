a = 'A'
b = 'B'
c = 1.1

string = '{para1} e {para1} e {para3:.5f}'
formato = string.format(para1=a, para2=b, para3=c)

print(formato)
