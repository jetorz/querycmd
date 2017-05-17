import sys
import webbrowser as wb

cmdlist = ['db']

cmd = sys.argv[1]

if cmd not in cmdlist:
    print('Unkonw command %s. Contact me for detail.' % cmd)
    out = input()
    sys.exit(0)

rest = sys.argv[2:]
key = ""
for r in rest:
    key += str(r) + ' '

# print(sys.argv[:])
# print(cmd)
# print(key)

# Douban book query.
if cmd == 'db':
    url = r'https://book.douban.com/subject_search?search_text=' + key + r'&cat=1003'
    wb.open_new_tab(url)
else:
    print('Unkonw command %s. Contact me for detail.' % cmd)
