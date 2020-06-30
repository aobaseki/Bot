class Product:
    def __init__(self, bot, chatObj, prevStage):
        self.bot = bot
        self.prevStage = prevStage
        self.user =  chatObj.message #complete this...
        self.chatId = chatObj.message.chat.id
        self.msgId = chatObj.message.message_id

        self.product_get = "Okay you want to add a product.\nWhat category of product do you want to add?\n Example: Guinness"
    def stage_zero(self):
        # fectch customer information from API and save in 
        # save ther users id, chatid and progress
        # then send a request for product catergory

    def stage_one(self, category):
        # find catergory
        # send confirmation
        self.bot.send_message(chat_id=self.chatId, text=self.product_get, reply_to_message_id=self.chatId)
        


