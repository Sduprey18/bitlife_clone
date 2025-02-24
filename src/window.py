import customtkinter
from src.person import Player
from src.stories import Stories

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x500")
        self.title("Bitlife Clone")
        customtkinter.set_appearance_mode("system")

        # Start button for the game
        self.createLifeButton = customtkinter.CTkButton(self, text="Create a random life!",
                                                        command=self.gameStatus, fg_color="yellow", text_color='black',
                                                        hover_color='gray')
        self.createLifeButton.grid(row=0, column=0, padx=225, pady=450)

    def destroyButton(self):
        self.createLifeButton.destroy()

    # Function to display age, money, call age up button
    def gameStatus(self):
        self.destroyButton()
        self.ageLabel = customtkinter.CTkLabel(self, text="Age", fg_color="yellow", text_color="black")
        self.ageLabel.grid(row=0, column=0, padx=75, pady=50)

        self.moneyLabel = customtkinter.CTkLabel(self, text="Money", fg_color="yellow", text_color="black")
        self.moneyLabel.grid(row=0, column=1, padx=25, pady=50)
        
        self.createLife()
        self.ageUpButton()

    # Function to make the age up button
    def ageUpButton(self):
        self.ageUpButton = customtkinter.CTkButton(self, text="Age up!", command=self.updateLabels, fg_color="yellow", text_color='black', hover_color='gray')
        self.ageUpButton.grid(row=1, column=0, columnspan=2, padx=225, pady=245, sticky='ew')
        print(self.player.age)

    def updateLabels(self):
        self.moneyLabel.configure(text=f"Money: ${self.player.getMoney()}")
        self.ageLabel.configure(text=f"Age : {self.player.getAge()}")
        self.storyText = Stories()
        self.birthLabel = customtkinter.CTkLabel(self, text =self.storyText.generateBirth(self.player.getPlaceOfBirth()))
        self.player.ageUp()

    #create the player 
    def createLife(self):
        self.player = Player( 0.0, 100, 0)

    #create the stats to show 
    def displayStats(self):
        self.ageText = customtkinter.CTkTextbox(self, width=200)  # Add the width parameter
        self.ageText.grid(row=2, column=0, columnspan=2)


app = App()
app.mainloop()
