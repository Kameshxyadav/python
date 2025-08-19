class employee:
    lang="python" #class attribute
    salary=1000
    
    def getinfo(self):
        print("the lang is {self.lang}. the salary is {self.salary}")
    @staticmethod
    def greet():
        print("hello")

harry=employee()
harry.greet()
harry.getinfo()