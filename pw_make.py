from string import ascii_letters, digits, punctuation #, ascii_lowercase, ascii_uppercase
from random import SystemRandom

if '__main__' == __name__:
    from sys import argv
    if len(argv) < 2 or not argv[1].isdecimal():
        print('usage  : <pwlength> [option] [-c]\n\
              [option]: combination of "p" punctuation / "a" ascii_letters / "d" digits\n\
              [-c]    : silently copy into clipboard')
        exit(1)
    option, rst, flag = '', '', ''
    if len(argv) > 2:
        if not argv[2] is '-c': option = argv[2]
        else:flag=argv[2]
        if len(argv)>3 and argv[3] is '-c': flag = argv[3]
    rst=''
    avail = (ascii_letters+digits+punctuation) if not option else \
            ((ascii_letters if 'a' in option else '') +
            (digits if 'd' in option else '') +
            (punctuation if 'p' in option else ''))
    for i in range(int(argv[1])):
        rst += SystemRandom().choice(avail)
    if rst and flag is '-c':
        toecho = ''
        for c in rst:
            toecho += ('^^^'+c) if c in '<|&>' else ('^'+c)if c in punctuation else c
        from sys import platform
        copycmd = '|clip'if platform is 'win32'else'>/dev/clipboard'if platform is 'cygwin'else'|pbcopy'if platform is 'darwin'else'|xclip'
        from os import system
        system('echo {}{}'.format(toecho, copycmd))
    else:
        print(rst)