def generateReprString(cls, name):
    return "{cls}('node')".format(cls=cls, node=rootName(name))

def rootName(name):
    pass