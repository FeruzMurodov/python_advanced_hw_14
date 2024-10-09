import pytest


class InsufficientFundsError(Exception):
    pass


class BankAccount:
    def __init__(self, initial_balance=0):
        self._count = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self._count += amount
        else:
            print('Minus value cant be added to count')

    def withdraw(self, amount):
        if amount < self._count:
            self._count -= amount
        else:
            raise InsufficientFundsError("There is no such amount of money in your count")

    def get_balance(self):
        return self._count


@pytest.fixture()
def initiation_class():
    return BankAccount()


def test_init(initiation_class):
    assert initiation_class._count == 0, "Count must be zero"


def test_deposit_norm(initiation_class):
    initiation_class.deposit(500)
    assert initiation_class._count == 500, "Something's wrong"


def test_deposit_wrong(initiation_class):
    initiation_class.deposit(-500)
    assert initiation_class.get_balance() == 0


def test_withdraw_norm(initiation_class):
    initiation_class.deposit(500)
    initiation_class.withdraw(400)
    assert initiation_class._count == 100, "Something's wrong"


def test_withdraw_wrong(initiation_class):
    initiation_class.deposit(500)
    with pytest.raises(InsufficientFundsError):
        initiation_class.withdraw(600)


def test_get_balance_after_init(initiation_class):
    assert initiation_class.get_balance() == 0


def test_get_balance_after_deposit(initiation_class):
    initiation_class.deposit(500)
    assert initiation_class.get_balance() == 500


if __name__ == '__main__':
    pytest.main(['-v'])
