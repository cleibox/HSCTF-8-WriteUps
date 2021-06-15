from pwn import *

def amino_acid(question):
    print(question)
    peptide = question.split(" ")[1]
    good = True
    for acid in peptide:
        if not acid in valid:
            p.sendline(b"F")
            good = False
            break
    if good:
        p.sendline(b"T")

def iv_thing(question):
    iv = question[-1]
p = remote("canis-lupus-familiaris-bernardus.hsc.tf", 1337)
valid = []
p.recv()
stuff = p.recv().decode("utf-8")
index = 0
for letter in stuff:
    if letter == ":":
        valid.append(stuff[index + 2])
    index += 1
question = stuff.splitlines()[-1]
amino_acid(question)

question = p.recv().decode("utf-8")
if "peptide" in question:
    amino_acid(question)
elif "IV" in question:
    print(">:( idk")
else:
    print("new question")
    print(question)
p.interactive()