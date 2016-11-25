def hello(name="World"):
    if name is None:
        return "Hello, World!"
    elif name == '':
        return "Hello, World!"
    elif type(name) is not str:
        return "Hello, %s!" % name
    else:
        return "Hello, World!"

print hello(name="World")
