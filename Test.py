prodname = 'geek for geeks'
prodword = prodname.split()
n = len(prodword)
print(n)

if n == 1:
    produrl = prodword[0]
else:
    produrl = prodword[0]
    for i in range(0, n - 1):
        produrl = str(produrl + '+' + prodword[i])

amazon = produrl
flipkart = produrl.replace('+', ' ', n - 1)
print(flipkart)