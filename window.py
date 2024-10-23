import customtkinter
from person import Player

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x500")
        self.title("Bitlife Clone")
        customtkinter.set_appearance_mode("system")

        #Start button for the game
        self.createLifeButton = customtkinter.CTkButton(self, text="Create a random life!",command=self.gameStatus, fg_color="yellow", text_color='black', hover_color='gray')
        self.createLifeButton.pack()
        self.createLifeButton.grid(row=0, column=0, padx=225, pady=450)
        
    def destroyButton(self):
        self.createLifeButton.destroy()
    
    #Function to display age, money, call age up button
    def gameStatus(self):
        self.destroyButton()
        self.ageLabel = customtkinter.CTkLabel(app, text="Age", fg_color="yellow", text_color="black")
        self.ageLabel.grid(row=0, column =0, padx =75, pady =50)

        self.moneyLabel = customtkinter.CTkLabel(app, text="Money", fg_color="yellow", text_color="black")
        self.moneyLabel.grid(row =0, column =1, padx = 25, pady=50, )
        self.ageUpButton()
        self.createLife()
        

    #function to make the age up button
    def ageUpButton(self):
        self.ageUpButton = customtkinter.CTkButton(self, text = "Age up!", fg_color="yellow", text_color='black', hover_color='gray')
        self.ageUpButton.grid(row=1, column=0, columnspan = 2, padx=225, pady=450, sticky='ew',)
        
    def createLife(self):
        self.player = Player("United States",0.0, 100, 0)
    
    def displayStats(self):
        self.ageText = customtkinter.CTkTextbox(app, width)





app = App()

app.mainloop()

