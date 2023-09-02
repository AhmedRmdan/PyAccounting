"""Owner's Equity accouts models"""
from account_class import Account


class OE(Account):
    """Owner's Equity accout model"""

    def __init__(self, name, balance, acc_type="cr"):
        super().__init__(name, balance, acc_type)

    balance_sheet = {}

    def update(self):
        """Updates the balance_sheet dict for every transaction"""
        self.__class__.balance_sheet[self.name] = self._balance, self._acc_type
        __class__.balance_sheet[self.name] = self._balance, self._acc_type


class Capital(OE):
    """Owner's Capital accout model"""

    def __init__(self, name, balance, acc_type="cr"):
        super().__init__(name, balance, acc_type)

    balance_sheet = {}


class Revenue(OE):
    """Revenues accout model"""

    def __init__(self, name, balance, acc_type="cr"):
        super().__init__(name, balance, acc_type)

    balance_sheet = {}


class Expense(OE):
    """Expenses accout model"""

    def __init__(self, name, balance, acc_type="dr"):
        super().__init__(name, balance, acc_type)

    balance_sheet = {}


class Drawing(OE):
    """Owner's drawings accout model"""

    def __init__(self, name, balance, acc_type="dr"):
        super().__init__(name, balance, acc_type)

    balance_sheet = {}