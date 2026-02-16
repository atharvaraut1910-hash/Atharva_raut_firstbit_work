class Account:

    def __init__(self, ac_no=0, holder_name='', balance=0, ac_type='Saving', branch='Pune'):
        self.ac_no = ac_no
        self.holder_name = holder_name
        self.balance = balance
        self.ac_type = ac_type
        self.branch = branch

    def getData(self):
        return f'''AC NO: {self.ac_no}
HOLDER NAME: {self.holder_name}
BALANCE: {self.balance}
TYPE: {self.ac_type}
BRANCH: {self.branch}'''


ac1 = Account(1001, 'ABC', 10000, 'Saving', 'FC Road')
print(ac1.getData())

print('###############')

ac2 = Account()
print(ac2.getData())
