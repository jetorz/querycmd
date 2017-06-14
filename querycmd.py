import sys, math
import webbrowser as wb

def about():
    wb.open_new_tab('about.html')

def dt():
    a = float(input('输入年投资额（元）：'))
    x = input('输入年化收益率百分比(8)：')
    print(x)
    if len(x) == 0:
        x=0.08
    else:
        x = float(x)/100
    print(x)
    n = int(input('输入定投年数（年）：')) * 1.0
    M = a*(1+x)*(-1+pow((1+x),n))/x
    print('定投结束后，总金额为：%.2f。' % M)
    input('Press any key to continue...')

cmd = str(sys.argv[1])
rest = sys.argv[2:]
query = ""
for r in rest:
    query += str(r) + ' '

cmdfile = open('engine.DongTalks', 'r',encoding='utf-8')

# built-in functions
cmddict = {'about': about, 'dt':dt}

for line in cmdfile.readlines():
    if line.startswith('#') or line.startswith('\n'):
        pass
    else:
        engine = line.split(sep='|')
        for i in range(0, len(engine)):
            engine[i] = engine[i].strip()
        if len(engine) == 3:
            before = engine[1].strip()
            after = ''
        else:
            after = engine[3]
        searchurl = before + query + after
        cmddict[engine[0]] = searchurl

print(cmd)
print(cmddict[cmd])

if cmd not in cmddict.keys():
    print('Unkonw command "%s". Contact me for detail.' % cmd)
    print('You know how to find me, do you? ;)')
    out = input()
    sys.exit(0)
else:
    if type(cmddict[cmd]) == str:
        wb.open_new_tab(cmddict[cmd])
    else:
        cmddict[cmd]()
