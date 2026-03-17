# by ASD & leejunheok discord : xg3w & fuckthefame1
import re

print("Wearedevs Obf(Prometheus) dumper by ASD & leejunheok")

target_ = "target.lua"
output_ = "output.lua"

with open(target_) as fuck:
    target_stringzhaha = fuck.read()

overtonight = re.compile(r'\b(\w+)=\w+\s*\.\.\s*\w+\b')

for porns in overtonight.findall(target_stringzhaha):
    print(f"[+] found important vars : {porns}")

def fu(m):
    return f'{m.group(0)} appendfile("dump.log", game:GetService("HttpService"):JSONEncode({{{m.group(1)}}}, true) .. "\\n")'

def ck(s):
    return f"{s.group(0)} print({s.group(1)})"

print("--Type 1 to dump in executor--")
print("--Type 2 to dump in rbx studio--")
ah = input("choice : ")
if ah=="1":
    print("saves in workspace/a.log")
    with open(output_, "w") as porn:
        porn.write(overtonight.sub(fu, target_stringzhaha))
elif ah=="2":
    with open(output_, "w") as porn:
        porn.write(overtonight.sub(ck, target_stringzhaha))
else:
    print("invalid choice")

print("check output.lua and run output.lua in your executor or rbx studio")
