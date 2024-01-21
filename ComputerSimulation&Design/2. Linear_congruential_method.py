
def congruential_random_generator(a):
    for i in range(len(a)):
        a[i] = int(a[i]) 
    x = a[2]
    y=[x]
    first = True
    k=13
    while  a[3]!=0 and k>0: x=(a[0]*x+a[1]) % a[3]; y.append(x); first &= 0; k-=1
    return y

with open('random_generator.txt') as file:
    lines = file.read().split('\n')
    lines = [line.split(' ') for line in lines]

output = [congruential_random_generator(line) for line in lines]
for i in range (len(output)):
    print('For generator', lines[i],'Random Numbers : ', output[i])