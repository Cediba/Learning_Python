class bank_account:
    _last_assigned_number = 1000 # Class Variable
    def __init__(self):
        self._balance = 0 # balance is a instance variable
        bank_account._last_assigned_number +=  1
        self._account_number = bank_account._last_assigned_number
print(bank_account._last_assigned_number)

ba1 = bank_account()
print(ba1._last_assigned_number)
ba2 = bank_account()
print(ba2._last_assigned_number)
print(bank_account._last_assigned_number)