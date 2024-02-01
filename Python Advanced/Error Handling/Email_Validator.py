from re import findall


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class MoreThanOneSymbol(Exception):
    pass


class InvalidNameError(Exception):
    pass


class InvalidStartOrEnd(Exception):
    pass


VALID_SYMBOLS = r"[A-Za-z0-9\.\_\-]+"
VALID_DOMAINS = ("com", "bg", "net", "org")
MIN_SYMBOL_COUNT = 4

email = input()

while email != "End":
    if email.count('@') > 1:
        raise MoreThanOneSymbol("Email should contain only one @ symbol!")
    if '@' not in email:
        raise MustContainAtSymbolError("Email should contain @ symbol!")
    if len(email.split('@')[0]) <= MIN_SYMBOL_COUNT:
        raise NameTooShortError("Name must be more than 4 characters")
    if findall(VALID_SYMBOLS, email.split("@")[0])[0] != email.split("@")[0]:
        raise InvalidNameError("Name must contain only digits, letters, '.', '_', '-'")
    if email.split(".")[-1] not in VALID_DOMAINS:
        raise InvalidDomainError(f"Domain must be: {", ".join("." + domain for domain in VALID_DOMAINS)}")
    if email.startswith(".") or email.endswith("."):
        raise InvalidStartOrEnd("Email can't start or end with '.'")

    print("Email is valid")

    email = input()



