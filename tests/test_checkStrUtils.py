import pytest
import lib.checkStrUtils as checkStrUtils


class TestClass:

    def testCheckIfStrIsCorrectLength(self):
        assert checkStrUtils.checkIfStrIsCorrectLength("", 8, 12) == False
        assert checkStrUtils.checkIfStrIsCorrectLength("aaaaaaa", 8,
                                                       12) == False
        assert checkStrUtils.checkIfStrIsCorrectLength("aaaaaaaa", 8,
                                                       12) == True
        assert checkStrUtils.checkIfStrIsCorrectLength("aaaaaaaaaa", 8,
                                                       12) == True
        assert checkStrUtils.checkIfStrIsCorrectLength("aaaaaaaaaaaa", 8,
                                                       12) == True
        assert checkStrUtils.checkIfStrIsCorrectLength("aaaaaaaaaaaaa", 8,
                                                       12) == False
        assert checkStrUtils.checkIfStrIsCorrectLength("aaaaaaaaaaaaaaaaaaaaa",
                                                       8, 12) == False

    def testCheckIfStrContainsUpperChar(self):
        assert checkStrUtils.checkIfStrContainsUpperChar("") == False
        assert checkStrUtils.checkIfStrContainsUpperChar("b") == False
        assert checkStrUtils.checkIfStrContainsUpperChar("1") == False
        assert checkStrUtils.checkIfStrContainsUpperChar("A") == True
        assert checkStrUtils.checkIfStrContainsUpperChar("bA") == True
        assert checkStrUtils.checkIfStrContainsUpperChar("bbbAAA") == True

    def testCheckIfStrContainsDigit(self):
        assert checkStrUtils.checkIfStrContainsDigit("") == False
        assert checkStrUtils.checkIfStrContainsDigit(
            "thereIsNoNumberHere") == False
        assert checkStrUtils.checkIfStrContainsDigit("1") == True
        assert checkStrUtils.checkIfStrContainsDigit("2") == True
        assert checkStrUtils.checkIfStrContainsDigit("3") == True
        assert checkStrUtils.checkIfStrContainsDigit("4") == True
        assert checkStrUtils.checkIfStrContainsDigit("5") == True
        assert checkStrUtils.checkIfStrContainsDigit("6") == True
        assert checkStrUtils.checkIfStrContainsDigit("7") == True
        assert checkStrUtils.checkIfStrContainsDigit("8") == True
        assert checkStrUtils.checkIfStrContainsDigit("9") == True
        assert checkStrUtils.checkIfStrContainsDigit("0") == True

        assert checkStrUtils.checkIfStrContainsDigit("a1") == True
        assert checkStrUtils.checkIfStrContainsDigit("a2") == True
        assert checkStrUtils.checkIfStrContainsDigit("a3") == True
        assert checkStrUtils.checkIfStrContainsDigit("a4") == True
        assert checkStrUtils.checkIfStrContainsDigit("a5") == True
        assert checkStrUtils.checkIfStrContainsDigit("a6") == True
        assert checkStrUtils.checkIfStrContainsDigit("a7") == True
        assert checkStrUtils.checkIfStrContainsDigit("a8") == True
        assert checkStrUtils.checkIfStrContainsDigit("a9") == True
        assert checkStrUtils.checkIfStrContainsDigit("a0") == True

        assert checkStrUtils.checkIfStrContainsDigit("a1a") == True
        assert checkStrUtils.checkIfStrContainsDigit("a2a") == True
        assert checkStrUtils.checkIfStrContainsDigit("a3a") == True
        assert checkStrUtils.checkIfStrContainsDigit("a4a") == True
        assert checkStrUtils.checkIfStrContainsDigit("a5a") == True
        assert checkStrUtils.checkIfStrContainsDigit("a6a") == True
        assert checkStrUtils.checkIfStrContainsDigit("a7a") == True
        assert checkStrUtils.checkIfStrContainsDigit("a8a") == True
        assert checkStrUtils.checkIfStrContainsDigit("a9a") == True
        assert checkStrUtils.checkIfStrContainsDigit("a0a") == True

        assert checkStrUtils.checkIfStrContainsDigit("1a") == True
        assert checkStrUtils.checkIfStrContainsDigit("2a") == True
        assert checkStrUtils.checkIfStrContainsDigit("3a") == True
        assert checkStrUtils.checkIfStrContainsDigit("4a") == True
        assert checkStrUtils.checkIfStrContainsDigit("5a") == True
        assert checkStrUtils.checkIfStrContainsDigit("6a") == True
        assert checkStrUtils.checkIfStrContainsDigit("7a") == True
        assert checkStrUtils.checkIfStrContainsDigit("8a") == True
        assert checkStrUtils.checkIfStrContainsDigit("9a") == True
        assert checkStrUtils.checkIfStrContainsDigit("0a") == True

    def testCheckIfStrContainsSpecialChar(self):
        # specialChars = ["!", "@", "#", "$", "%", "^", "&", "*", "-", "_"]
        assert checkStrUtils.checkIfStrContainsSpecialChar("") == False
        assert checkStrUtils.checkIfStrContainsSpecialChar("!") == True
        assert checkStrUtils.checkIfStrContainsSpecialChar("@") == True
        assert checkStrUtils.checkIfStrContainsSpecialChar("#") == True
        assert checkStrUtils.checkIfStrContainsSpecialChar("$") == True
        assert checkStrUtils.checkIfStrContainsSpecialChar("%") == True
        assert checkStrUtils.checkIfStrContainsSpecialChar("^") == True
        assert checkStrUtils.checkIfStrContainsSpecialChar("&") == True
        assert checkStrUtils.checkIfStrContainsSpecialChar("*") == True
        assert checkStrUtils.checkIfStrContainsSpecialChar("-") == True
        assert checkStrUtils.checkIfStrContainsSpecialChar("_") == True
