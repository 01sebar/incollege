def checkIfStrIsCorrectLength(str, min, max):
    if len(str) >= min and len(str) <= max:
        return True
    return False


#testable
def checkIfStrContainsUpperChar(str):
    for char in str:
        if char.isupper():
            return True
    return False


#testable
def checkIfStrContainsDigit(str):
    for char in str:
        if char.isdigit():
            return True
    return False


#testable
def checkIfStrContainsSpecialChar(str):
    specialChars = ["!", "@", "#", "$", "%", "^", "&", "*", "-", "_"]
    for char in str:
        if char in specialChars:
            return True
    return False
