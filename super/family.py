class Adam(object): pass

class Eve(object): pass

class Ramon(Adam, Eve): pass

class Gayle(Adam, Eve): pass

class Raymond(Ramon, Gayle): pass

class Dennis(Adam, Eve): pass

class Sharon(Adam, Eve): pass

class Rachel(Dennis, Sharon): pass

class Matthew(Raymond, Rachel): pass

help(Matthew)
