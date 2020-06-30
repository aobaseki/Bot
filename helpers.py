def is_command(text):
    return text[0] == "/"

def sayHello(user):
    return """Hello {}, Welcome to My STORE AID \nPlease enter one of the following commands\n/sell\n\n/collection\n/addproduct\n/addstock""".format(user)


def displayHelp():
    return ""

def sell():
    return 

def selectCommand(command):
    if command == "addproduct":
        # begin a new command squence
        pass
    if  command == "addstock":
        # begin new command sequence
        pass
    if command == "sell":
        # begin a new command sequence
        pass
    if command == "start":
        # say hello
        pass

    if command == "end":
        # say goodbaye
        pass
    else:
        # repeat say hello
        pass

def continueConversation(lastChat):
    return

def addproduct(user, chatId, **kwargs):
    return











def getReponse(text, user = ""):
    if text["/"] != -1:
        if text == "/start":
            return sayHello(user)

        elif text == "/addproduct":
            return """You want to add a new product\nPlease send me the product name\n"""
        elif text == "/addstock":
            return """You want to add a new stock\nPlease send me the product name\n"""
        else:
         return "Hi I don't understand"
    else:
        return "Ok"

