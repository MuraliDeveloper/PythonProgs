"""
#requiremnet:
RBI is a parent class
SBI , HDFC , ICICI are the child classes for RBI

RBI: Parent class has
       - createAccount()
       - processLoan()

 ICICI WANTS TO GIVE RATE OF ROI @ 15%



#solution:????
no need of logic from parent
logic should come only from child
======> method overriding [replace the parent logic]
parent and child class will have the same methodName
but with diff logic 

Logic will come from child class:::
"""


class RBI:
    def createAccount(self):
        print("RBI:: account created")

    def processLoan(self):
        print("RBI:: roi 10%")


class SBI(RBI):
    def demat1(self):
        print("SBI demat")


class HDFC(RBI):
    def demat2(self):
        print("HDFC demat")


class ICICI(RBI):
    def demat3(self):
        print("ICICI demat")

    def processLoan(self):
        print("ICICI:: roi 15%")


"""
for icici we have 3 type sof methods:
createAccount()  -> inherited method
processLoan() -> overriden method
demat() -> child specific method
"""

#crate obj
print("**********SBI**********")
sbi = SBI()
sbi.createAccount() # LOGIC FROM RBI
sbi.processLoan() # LOGIC FROM RBI
sbi.demat() # LOGIC FROM SBI

print("**********HDFC**********")
h = HDFC()
h.createAccount()# LOGIC FROM RBI 
h.processLoan()# LOGIC FROM RBI
h.demat() # LOGIC FROM HDFC

print("**********ICICI**********")
i = ICICI()
i.createAccount() # LOGIC FROM RBI
i.processLoan() # LOGIC FROM ICICI
i.demat() # LOGIC FROM ICICI
        