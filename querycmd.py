import sys
import webbrowser as wb

cmd = sys.argv[1]
rest = sys.argv[2:]
key = ""
for r in rest:
    key += str(r) + ' '

cmdfile = open('engine.DongTalks', 'r',encoding='utf-8')

cmddict = {}
for line in cmdfile.readlines():
    if line.startswith('#'):
        pass
    else:
        engine = line.split(sep='|')
        before = engine[1].strip()
        if len(engine) == 3:
            after = ''
        else:
            after = engine[3].strip()
        cmddict[engine[0].strip()] = before + key + after

if cmd not in cmddict.keys():
    print('Unkonw command "%s". Contact me for detail.' % cmd)
    print('You know how to find me, do you? ;)')
    out = input()
    sys.exit(0)

print(cmddict[cmd])

wb.open_new_tab(cmddict[cmd])
