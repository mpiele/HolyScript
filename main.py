print("WELCOME,")
print("HOLY SCRIPT VERSION 1.0")

def getCodeFile():
    code_file_name = input("Name of your .txt code file:")
    try:
        code_file = open(code_file_name, "r")
    except:
        print("ERROR: No file found")
        getCodeFile()
    else:
        return code_file.read()

getCodeFile()
