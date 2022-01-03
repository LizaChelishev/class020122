def get_salary(amount):
    if type(amount) != float:
        raise ValueError


class SalaryInputs:
    def __init__(self, amount):
        self.amount = amount

        