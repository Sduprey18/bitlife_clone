import customtkinter
from src.person import Player
from src.stories import Stories
from src.labels import Label
from src.randomEventsView import RandomEventFrame


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x500")
        self.title("Bitlife Clone")
        customtkinter.set_appearance_mode("system")

        
        self.createLifeButton = customtkinter.CTkButton(
            self, text="Create a random life!",
            command=self.gameStatus, fg_color="yellow", text_color='black',
            hover_color='gray'
        )
        self.createLifeButton.grid(
            row=0, column=0, padx=20, pady=20) 

    def destroyButton(self):
        self.createLifeButton.destroy()

    # Function to display age, money, happiness, call age up button
    def gameStatus(self):
        self.destroyButton()
       
        self.createLife()
        
        self.ageLabel = customtkinter.CTkLabel(
            self, text=f"Age: {self.player.getAge()}", fg_color="yellow", text_color="black")
        self.ageLabel.grid(row=0, column=0, padx=0, pady=0, sticky="w")

        self.moneyLabel = customtkinter.CTkLabel(
            self, text=f"Money: ${self.player.getMoney()}", fg_color="yellow", text_color="black")
        self.moneyLabel.grid(row=1, column=1, padx=0, pady=0, sticky="w")

        self.happinessLabel = customtkinter.CTkLabel(self, text=f"Happiness: {self.player.getHappiness()}",fg_color = "yellow", text_color = "black")
        self.happinessLabel.grid(row=1, column=0, padx=0, pady=0, sticky="w")

        self.healthLabel = customtkinter.CTkLabel(self, text=f"Health: {self.player.getHealth()}",fg_color="yellow", text_color="black")
        self.healthLabel.grid(row =3 , column = 0, padx = 0, pady = 0, sticky = 'w')


        self.ageUpButton()

   
    def ageUpButton(self):
        self.ageUpBtn = customtkinter.CTkButton(
            self, text="Age up!", command=self.updateLabels, fg_color="yellow", text_color='black', hover_color='gray'
        )
        self.ageUpBtn.grid(row=16, column=0, columnspan=2,
                           padx=20, pady=20, sticky='ew')

    def updateLabels(self):
        self.player.ageUp()
        self.testThing = RandomEventFrame(self, self.player)
        self.testThing.grid(
            row=0, column=1, padx=10, pady=(10, 0))
        
        self.moneyLabel.configure(text=f"Money: ${self.player.getMoney()}")
        self.ageLabel.configure(text=f"Age: {self.player.getAge()}")
        self.happinessLabel.configure(text=f"Happiness: {self.player.getHappiness()}")
        self.healthLabel.configure(text=f"Health: {self.player.getHealth()}")

    
    def createLife(self):
        self.player = Player(0.0, 100, 0)
        self.storyText = Stories()
        self.textLabel = Label(self)
        self.textLabel.grid(row=1, column=0, rowspan = 2, columnspan=2,
                             padx=20, pady=10, sticky='ew')
        self.textLabel.addText(self.storyText.generateBirth(
            self.player.getPlaceOfBirth()))

    
    def displayStats(self):
        self.ageText = customtkinter.CTkTextbox(self, width=200)
        self.ageText.grid(row=3, column=0, columnspan=2, padx=20, pady=10)


app = App()
app.attributes("-fullscreen", True)  #make fullscreen for mac
app.bind("<Escape>", lambda e: app.attributes("-fullscreen", False))


for i in range(16): 
    app.grid_rowconfigure(i, weight=1)

for j in range(2):  
    app.grid_columnconfigure(j, weight=1)

app.mainloop()

