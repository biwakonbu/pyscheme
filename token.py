# 空白文字
tSPACE = frozenset(' \n')
# コメント ;
tCOMMENT = frozenset(';')
tATMOSPHERE = (tSPACE, tCOMMENT)
# トークン間スペース ATMOSPHERE*
tTOKEN_SPACE = (tATMOSPHERE,)
# 開きカッコ
tSTART_PAREN = frozenset('(')
tCLOSE_PAREN = frozenset(')')
# ベクトル
tVECTOR = frozenset(['#('])
tQUOTE = frozenset('\'')
tBACK_QUOTE = frozenset('`')
tCOMMA = frozenset(',')
tQUASIQUOTE = frozenset([',@'])
tDOT = frozenset('.')

# 数字 0-9
tNUMBERS = frozenset('0123456789')
# 英字 a-zA-Z
tALPHABET = frozenset('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
# 特殊頭文字 !$%&*/:<=>?^_~
tSPECIAL_INITIAL_CHARACTER = frozenset('!$%&*/:<=>?^_~')
# 頭文字 <英字> | <特殊頭文字>
tINITIAL_CHARACTER = (tALPHABET, tSPECIAL_INITIAL_CHARACTER)
# 特殊後続文字 +-.@
tSPECIAL_AFTER_CHARACTER = frozenset('+-.@')
# 後続文字 <INITIAL_CHARACTER> | <NUMBERS> | <SPECIAL_AFTER_CHARACTER>
tAFTER_CHARACTER = (tINITIAL_CHARACTER, tNUMBERS, tSPECIAL_AFTER_CHARACTER)
# 識別子 <頭文字><後続文字>* | <独特な識別子>
tUNIQUE_IDENTIFIER = frozenset('+-*/')
tIDENTIFIER = ((tINITIAL_CHARACTER, tAFTER_CHARACTER), tUNIQUE_IDENTIFIER)
# ブーリアン #t | #f
tBOOLEAN = frozenset(['#t', '#f'])
# 進数
tBINARY = frozenset(['#b'])
tOCTAL = frozenset(['#o'])
tHEX = frozenset(['#x'])
# 数 <2進数> | <8進数> | <10進数> | <16進数>
tNUMBER = ((tBINARY, tNUMBERS), (tOCTAL, tNUMBERS), (tNUMBERS,), (tHEX, tNUMBERS))
# 文字
tCHARACTER_LITERAL = frozenset(['#\\'])
# 制御文字
tCHARACTER_NAME = frozenset(['space', 'newline'])
tCHARACTER = ((tCHARACTER_LITERAL, tALPHABET), (tCHARACTER_LITERAL, tCHARACTER_NAME))
tSTRING_NOT_FACTOR = frozenset(['"', '\\'])
tSTRING_TERMINATE = frozenset(['\"', ])
tSTRING = ((tSTRING_TERMINATE, tSTRING_NOT_FACTOR, tSTRING_TERMINATE),)

# トークン
tTOKEN =(
    tIDENTIFIER, tBOOLEAN, tNUMBER, tNUMBER, tCHARACTER, tSTRING,
    tSTART_PAREN, tCLOSE_PAREN, tVECTOR, tQUOTE, tBACK_QUOTE, tCOMMA,
    tQUASIQUOTE, tDOT
)

tEXPRESSION_KEYWORD = frozenset([
    'quote', 'lambda', 'if', 'set!', 'begin', 'cond',
    'and', 'or', 'case', 'let', 'let*', 'letrec', 'do', 'delay', 'quasiquote'
])

tSYNTAX_KEYWORD = (tEXPRESSION_KEYWORD, frozenset(['else', 'define', 'unquote', 'unquote-splicing']))

class TOKEN:
    def __init__(self, token, level=0):
        self.token = token
        self.level = level

    def __str__(self):
        return ((self.level*2)*' ')+'<'+self.__class__.__name__+' '+repr(self.token)+'>'

class START_PAREN(TOKEN):
    pass

class CLOSE_PAREN(TOKEN):
    pass

class SPACE(TOKEN):
    pass
