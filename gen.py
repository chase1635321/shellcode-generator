import os

cmd = "temp"
os.system("clear")
print("Commands: compile, run, generate")

while cmd != "exit":
    cmd = input()
    if cmd == "compile":
        print("gcc exec.c -fno-stack-protector -z execstack -o exec.x")
        os.system("gcc exec.c -fno-stack-protector -z execstack -o exec.x")
    if cmd == "run":
        os.system("./exec.x")
    if cmd == "clear":
        os.system("clear")
    if cmd == "generate":
        os.system("gcc shellcode.c -o shellcode.x");
        os.system("./generate_shellcode.sh")
