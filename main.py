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
        code_file_content = code_file.read().splitlines()

        return code_file_content

def runCode():
    tmp_code_file_content = getCodeFile()
    
    for code_line in tmp_code_file_content:
        code_line = code_line.strip()

        if code_line[0] == "p":
            final_print_text = ""
            is_bracket = False

            for character in code_line:
                if character == "(":
                    is_bracket = True
                elif character == ")":
                    is_bracket == False

                if is_bracket == True:
                    final_print_text += character
            
            final_print_text = final_print_text[1:-1]
            print(final_print_text)

        elif code_line[0] == "!":
            print("COMMENT LINE")
            
            
        else:
            print("NOT RECOGNIZED")

runCode()

