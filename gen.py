import os

cmd = "temp"
os.system("clear")
print("Commands: compile, run, generate")

while cmd != "exit":
    cmd = input()
    if cmd == "compile":
        print("gcc src/exec.c -fno-stack-protector -z execstack -o src/exec.x")
        os.system("gcc src/exec.c -fno-stack-protector -z execstack -o src/exec.x")
    if cmd == "run":
        os.system("./src/exec.x")
    if cmd == "clear":
        os.system("clear")
    if cmd == "generate":
        os.system("gcc src/shellcode.c -o src/shellcode.x");
        os.system("./src/generate_shellcode.sh")
