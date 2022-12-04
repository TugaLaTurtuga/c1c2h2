from math import sqrt
h = (" \033[31;4mc1**2=h**2-c2**2\033[m ")
print("{:=^57}" .format(" \033[31;4mh**2=c1**2+c2**2\033[m "))
n1 = float(input("\033[33mc1 = "))
n2 = float(input("\033[33mc2 = "))
ex17 = n1**2 + n2**2
print("h1 = \033[31m?\033[m\n\033[31m?**2\033[m = c1**2 + c2**2\n\033[31m?**2\033[m = {} + {}\n\033[31m?**2\033[m = \033[34;4m+-({})\033[m\n\033[31m?\033[m = \033[36m{}\033[m, pois ? > 0".format(n1**2, n2**2, ex17, sqrt(ex17)))
print("{:=^47}\n" .format("="))
print("{:=^57}" .format(h))
n3 = float(input("\033[33mh1 = "))
n4 = float(input("\033[33mc1 ou c2 = "))
nn3 = n3**2
nn4 = n4**2
nnr = nn3 - nn4
nnrq = pow(nnr, 1/2)
print("c2 ou c1 = {}\n{} = {} + {}\n{} = {} - {}\n{} = \033[34;4m+-({})\033[m\n{} = \033[36;4m{}\033[m, pois ? > 0" .format("\033[31m?\033[m", nn3, nn4, "\033[31m?**2\033[m", "\033[31m?**2\033[m",nn3, nn4, "\033[31m?**2\033[m", nnr, "\033[31m?\033[m",nnrq))
print("{:=^47}\n" .format("="))

#print("{:=^50}".format("\033Formação de triângulos\033[m"))
#r1 = float(input("\033[33mCumprimento do lado1 (a):"))
#r2 = float(input("\033[33mCumprimento do lado2 (b):"))
#r3 = float(input("\033[33mCumprimento do lado3 (c):"))
#if r1 + r2 > r3 and r2 + r3 > r1 and r3 + r1 > r2:
#    print("\033[32mO triângulo ABC pode ser formado pelos lados:\033[m\n\033[31;4m{}(a), {}(b) e {}(c)\033[m ".format(r1, r2, r3))
#else:
#    print("\033[32mO triângulo ABC não pode ser formado pelas retas:\033[m\n\033[31;4m{}(a), {}(b) e {}(c)\033[m ".format(r1, r2, r3))