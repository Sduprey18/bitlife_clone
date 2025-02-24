
jobType =[['Athlete'], ['Finance'], ['Tech'], ['Entertainment'], ['Creative'], ['Other']]


class Job:
   

    def __init__(self, job, salary: float, chosenJobType):
        self.job = job
        self.salary = salary
        self.chosenJobType = chosenJobType
    
    def setJob(self, job):
        self.job = job
    
    def setSalary(self, salary: float):
        self.salary = salary
    
    def jobRaise(self, salary: float) -> float:
        if self.chosenJobType ==['Athlete']:
            self.salary = (self.salary * .25) + self.salary
        elif self.chosenJobType ==['Finance']:
            self.salary = (self.salary * 5) + self.salary
        elif self.chosenJobType ==['Tech']:
            self.salary = (self.salary * .15) + self.salary
        elif self.chosenJobType ==['Entertainment']:
            self.salary = (self.salary * .05) + self.salary
        elif self.chosenJobType ==['Creative']:
            self.salary = self.salary + self.salary
        elif self.chosenJobType ==['Other']:
            self.salary = (self.salary * .30) + self.salary
        return self.salary
