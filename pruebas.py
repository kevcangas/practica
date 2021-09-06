from numpy.random import rand
""""
went = [rand(35),rand(35),rand(35),rand(35),rand(35),rand(35),rand(35),rand(35)]

wneu = [rand(2),rand(2),rand(2),rand(2),rand(2),rand(2),rand(2),rand(2)]

print(went[2][0])
"""
went=[]

archivo = open("pesos.txt","r")
for i in archivo:
    if(i[0] != "  "):
        went.append(i)

print(went[1])
