import customtkinter

class Label(customtkinter.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master)
    
    def addText(self, customText):
        self.customLabel = customtkinter.CTkLabel(self, text=customText)

