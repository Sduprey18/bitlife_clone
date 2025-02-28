import customtkinter
from src.events import Events


class RandomEventFrame(customtkinter.CTkFrame):
    def __init__(self, master, person) -> None:
        super().__init__(master)
        self.person = person
        
        self.randomEvents = Events(self.person)
        if self.person.age<18:
            self.generateBabyEvent()
        
        self.closeButton = customtkinter.CTkButton(self, text="Close", command=self.closeFrame)
        self.closeButton.grid(row=0, column=1, padx=10,
                          pady=(10, 0), sticky="w")

    
    def generateBabyEvent(self) -> None:
        randomText = self.randomEvents.randomEventBaby()
        self.textBox = customtkinter.CTkLabel(self, text=randomText, fg_color='gray', text_color='black')
        self.textBox.grid(row=0, column=0, padx=10,
                             pady=(10, 0), sticky="w")
    
    def closeFrame(self) -> None:
        self.destroy()
        

    
    