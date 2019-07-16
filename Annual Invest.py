  #9.2
from tkinter import * # Import tkinter

class Investment:
    def __init__(self):
        window = Tk() #Create a window
        window.title("Invesment Calculator") #Set title

        Label(window, text = "Invesment Amount").grid(row = 1, column = 1,
                sticky = W)
        Label(window, text = " Years").grid(row = 2, 
            column = 1, sticky = W)
        Label(window, text = "Annual Interest Rate").grid(row = 3, 
            column = 1, sticky = W)
        Label(window, text = " Future Value").grid(row = 4, 
            column = 1, sticky = W)


        self.investmentAmountVar = StringVar()
        Entry(window, textvariable = self.investmentAmountVar,
             justify = RIGHT).grid(row = 1, column =2)

        self.yearsVar = StringVar()
        Entry(window, textvariable = self.yearsVar,
              justify = RIGHT).grid(row = 2, column = 2)

        self.annualInterestRateVar = StringVar()
        Entry(window, textvariable = self.annualInterestRateVar, 
            justify = RIGHT).grid(row = 3, column = 2)
        
        self.futureValueVar = StringVar()
        lblFutureValue = Label(window, textvariable = 
            self.futureValueVar).grid(row = 4, 
                column = 2, sticky = E)

        Button(window, text = "Compute",command =
                           self.computeFutureValue).grid( row = 5, column = 2, sticky = E)

        window.mainloop() # Create an event loop
    def computeFutureValue(self):
      futureValue = self.getFutureValue(
          float(self.investmentAmountVar.get()),
          float(self.annualInterestRateVar.get())/ 1200,
          int(self.yearsVar.get()))
      self.futureValueVar.set(format(futureValue, '10.2f'))

      

    def getFutureValue(self, investmentAmount, monthlyInterestRate, years):
       
        futureValue = investmentAmount * ((1 + monthlyInterestRate )**(years*12))
        return futureValue
        
    


Investment()
