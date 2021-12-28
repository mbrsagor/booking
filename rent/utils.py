from enum import IntEnum


class TYPES(IntEnum):
    FLAT = 0
    ROOM = 1

    @classmethod
    def select_types(cls):
        return [(key.value, key.name) for key in cls]


class SEX(IntEnum):
    MALE = 0
    FEMALE = 1
    OTHERS = 2

    @classmethod
    def select_sex(cls):
        return [(key.value, key.name) for key in cls]


class MARITAL(IntEnum):
    UNMARRIED = 0
    MARRIED = 1

    @classmethod
    def select_status(cls):
        return [(key.value, key.name) for key in cls]


class ROLE(IntEnum):
    CUSTOMER = 0
    MANAGER = 1
    ACCOUNT = 2
    ADMIN = 3

    @classmethod
    def select_role(cls):
        return [(key.value, key.name) for key in cls]


class STATUS(IntEnum):
    PENDING = 0
    FAILED = 1
    PROGRESS = 2
    DONE = 3

    @classmethod
    def get_status(cls):
        return [(key.value, key.name) for key in cls]


class PAYMENT(IntEnum):
    BANK = 0
    PAYPAL = 1
    MASTERCARD = 2
    BKASH = 3
    NOGOD = 4
    UPAY = 5
    CASH = 6
    DUE = 7

    @classmethod
    def select_payment(cls):
        return [(key.value, key.name) for key in cls]
