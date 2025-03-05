import customtkinter
from src.events import Events


class RandomEventFrame(customtkinter.CTkFrame):
    def __init__(self, master, person,windows) -> None:
        super().__init__(master)
        self.windows = windows
        self.person = person
        
        self.randomEvents = Events(self.person)
        if self.person.age<18:
            self.closeAllFrames()
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
        print("hi")
    
    def closeFrame(self) -> None:
        self.windows -=1
        self.destroy()
    
    def closeAllFrames(self) -> None:
        while self.windows> 0:
            print(f"hi {self.windows}")
            self.windows -=1
            self.destroy()
            
        if self.winfo_exists():      
            self.generateBabyEvent()
    
    def windowExists(self) -> None:
        return self.windows != 0
        

    
    