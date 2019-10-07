import sys, math, os, platform, subprocess
import webbrowser as wb

DEBUGMODE = False

def dPrint(x, pairs=locals().items()):
    if DEBUGMODE == False:
        return
    varlist = []
    for (k, v) in pairs:
        if v == x:
            varlist.append((k, v))
    dbg = open('dbg.txt', mode='a', encoding='utf8')
    print('%s => %s' % (varlist[0][0], x), file=dbg)

def PraseEngine(cmdfile):
    cmddict = {}
    for line in cmdfile:
        line = line.split()
        key = line[1]
        before = line[2]
        after = ''
        if len(line) > 4:
            for i in range(4,len(line)):
                after = after + line[i]
        cmddict[key] = {'before':before, 'after':after}
    return cmddict

if __name__ == "__main__":
    if DEBUGMODE == True:
        dbg = open('dbg.txt', mode='w', encoding='utf8')
        dbg.close()

    dbg = open('dbg.txt', 'a', encoding='utf8')
    argv = sys.argv
    dPrint(argv)
    cmdfile = open('engine.txt', 'r', encoding='utf-8')
    engine = PraseEngine(cmdfile)
    dPrint(engine)

    cmd = argv[1].lower()
    dPrint(cmd)
    query = ''
    if cmd in engine.keys():
        for i in range(2, len(argv)):
            query = query + argv[i] + ' '
        surl = engine[cmd]['before'] + query + engine[cmd]['after']
        dPrint(surl)
    else:
        for i in range(1, len(argv)):
            query = query + argv[i] + ' '
        surl = engine['g']['before'] + query
        dPrint(surl)

    wb.open_new_tab(surl)