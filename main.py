import token

tokens = []
with open('sample.scm', 'r') as f:
    exp = []
    t = ''
    level = 0
    while True:
        ch = f.read(1)

        if not len(ch):
            break

        if ch in token.tSTART_PAREN:
            exp.append(token.START_PAREN(ch, level))
            level += 1
        elif ch in token.tSPACE:
            exp.append(token.TOKEN(t, level))
            t = ''
            # exp.append(token.SPACE(ch, level))
        elif ch in token.tCLOSE_PAREN:
            exp.append(token.TOKEN(t, level))
            t = ''
            level -= 1
            exp.append(token.CLOSE_PAREN(ch, level))
            tokens.append(exp)
        else:
            t += ch

for exp in tokens:
    for t in exp:
        print(t)
