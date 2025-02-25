import customtkinter

class Label(customtkinter.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master)
        for i in range(2):
            self.grid_rowconfigure(i, weight=1)
    
    def addText(self, customText):
        self.customLabel = customtkinter.CTkLabel(self, text=customText, fg_color="gray", text_color="black")
        self.customLabel.grid(row=2, column=0,
                              padx=20, pady=10, sticky='ew')
        #self.customLabel = customtkinter.CTkLabel(self, text=customText)

