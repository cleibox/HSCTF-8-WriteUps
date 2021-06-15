from pwn import *

def not_math(question):
    print(question)
    mult = question.split("m")
    for i in range(len(mult)):
        add = mult[i].split("a")
        if len(add) > 1:
            added_sum = 0
            for j in add:
                if j != "":
                    added_sum += int(j)
                mult[i] = added_sum
        else:
            if mult[i] != "":
                mult[i] = int(mult[i])
    print(mult)
    product = 1
    for i in mult:
        if i != "":
            product *= i
    print(product%4294967295)
    return product%4294967295
# print(not_math("74a95a91m32m28a15m99m44m69a88")) # 260 x 32 x 43 x 99 x 44 x 157
p = remote("not-really-math.hsc.tf", 1337)
# p.interactive()
p.recv()
# while p.can_recv:
def do_stuff(): 
    inp = p.recv().decode("utf-8")
    if ":" in (inp.splitlines()[0]):
        inp = p.recv().decode("utf-8")
    print(inp)
    p.sendline(str(not_math(inp.splitlines()[0])).encode())
for i in range(5):
    do_stuff()

p.interactive()