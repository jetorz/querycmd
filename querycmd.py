import sys
import webbrowser as wb

cmdlist = ['db','bd']

cmd = sys.argv[1]

if cmd not in cmdlist:
    print('Unkonw command %s. Contact me for detail.' % cmd)
    out = input()
    sys.exit(0)

rest = sys.argv[2:]
key = ""
for r in rest:
    key += str(r) + ' '

# Douban book query.
if cmd == 'db':
    url = r'https://book.douban.com/subject_search?search_text=' + key + r'&cat=1003'
    wb.open_new_tab(url)
elif cmd =='bd':
    url = r'https://www.baidu.com/s?wd=' + key
    wb.open_new_tab(url)
else:
    print('Unkonw command %s. Contact me for detail.' % cmd)
