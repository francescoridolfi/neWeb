def get_result(args):
    try:
        name = args["name"]
    except:
        name = "Try this: <a href='/?name=Francesco'>click here</a>"
    chars = {
        "setname":{
            "char":"%name","method":str(name)
        }
    }
    file_name = "index.html"

    HTML = [chars,file_name]
    return HTML
