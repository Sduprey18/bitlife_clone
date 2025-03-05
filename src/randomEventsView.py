import customtkinter
from src.events import Events


class RandomEventFrame(customtkinter.CTkFrame):
    def __init__(self, master, person,windows) -> None:
        super().__init__(master)
        self.windows = windows
        self.person = person
        #self.frames = []
        
        self.randomEvents = Events(self.person)
        if self.person.age<18:
            self.generateBabyEvent()
            print("hi")
        
        self.closeButton = customtkinter.CTkButton(self, text="Close", command=self.closeFrame)
        self.closeButton.grid(row=0, column=1, padx=10,
                          pady=(10, 0), sticky="w")
        

    
    def generateBabyEvent(self) -> None:
        randomText = self.randomEvents.randomEventBaby()
        self.textBox = customtkinter.CTkLabel(self, text=randomText, fg_color='gray', text_color='black')
        self.textBox.grid(row=0, column=0, padx=10,
                             pady=(10, 0), sticky="w")
        self.windows +=1
        
    
    def closeFrame(self) -> None:
        self.windows -=1
        self.destroy()
    

        

    
    