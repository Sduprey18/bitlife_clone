import customtkinter
import tkinter

class Label(customtkinter.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master)
        for i in range(2):
            self.grid_rowconfigure(i, weight=1)
        
       
        #self.grid_rowconfigure(0, weight=1)
        self.current_row = 0
    
    def addText(self, customText):
        self.customLabel = customtkinter.CTkLabel(self, text=customText, fg_color="gray", text_color="black", anchor ="center", corner_radius=15)
        self.customLabel.grid(row=self.current_row, column=0,
                              padx=2, pady=10, sticky='s')
        
        #self.customLabel = customtkinter.CTkLabel(self, textcustomText)
        self.current_row += 1
    
   