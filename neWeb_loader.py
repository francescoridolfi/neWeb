import sys, os


paths = []
pages = []

HTMLs = []

def start(args):
    paths = os.listdir("py-page")
    for file in paths:
        if(file.endswith(".py")):
            dot_pos = len(file) - 3
            pages.append(file[:dot_pos])

    sys.path.insert(0, "py-page")

    for page in pages:
        load = __import__(page)

        HTMLs.append(load.get_result(args))
    return HTMLs
