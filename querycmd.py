import sys, math, os, platform, subprocess
import webbrowser as wb

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
    dbg = open('dbg.txt', 'w', encoding='utf8')
    argv = sys.argv
    print('argv=> %s' % argv, file=dbg)
    cmdfile = open('engine.txt', 'r', encoding='utf-8')
    engine = PraseEngine(cmdfile)
    print('engine => %s.' % engine, file=dbg)

    cmd = argv[1].lower()
    print('cmd=>%s ' % cmd, file=dbg)
    query = ''
    if cmd in engine.keys():
        print(cmd + ' is in engine.', file=dbg)
        for i in range(2, len(argv)):
            query = query + argv[i] + ' '
        surl = engine[cmd]['before'] + query + engine[cmd]['after']
        print('seach url is:' + surl, file=dbg)
    else:
        print(cmd + ' is not in engine.', file=dbg)
        for i in range(1, len(argv)):
            query = query + argv[i] + ' '
        surl = engine['g']['before'] + query

    wb.open_new_tab(surl)
    dbg.close()