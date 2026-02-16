from emp import Employee
from datastore import Datastore

class Admin:
    def __init__(self):
        self.ds = Datastore()
        ch = 0
        while(ch != '6'):
            print('#####ADMIN#####')
            print('''Please select option from below:
                  1.Add employee
                  2.Update employee
                  3.Search employee
                  4.Show all employee
                  5.Delete employee
                  6.Logout
                  ''')
            ch = input('Enter choise:')
            if(ch == '1'):
                self.addEmp()
            elif(ch == '2'):
                self.upEmp()
            elif(ch == '3'):
                self.searchEmp()
            elif(ch == '4'):
                self.showAllEmp()
            elif(ch == '5'):
                self.delEmp()
            elif(ch == '6'):
                print('Logged out seccesfully...')
            else:
                print('Invalid choise...')

    def addEmp(self):
        pass
    def upEmp(self):