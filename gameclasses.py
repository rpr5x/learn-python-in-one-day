class Game:
    """
    A base class for our games that contains a getter and setter for the number of questions (noOfQuestions) in the game
    """

    def __init__(self, noOfQuestions=0):
        self._noOfQuestions = noOfQuestions

    @property
    def noOfQuestions(self):
        return self._noOfQuestions

    @noOfQuestions.setter
    def noOfQuestions(self, value):
        if value < 1:
            self._noOfQuestions = 1
            print("\nMinimum Number of Questions = 1")
            print("Hence, number of questions will be set to 1")
        elif value > 10:
            self._noOfQuestions = 10
            print("\nMaximum Number of Questions = 10")
            print("Hence, number of questions will be set to 10")
        else:
            self._noOfQuestions = value


class BinaryGame(Game):
    """
    The BinaryGame class that inherits from our base Game class. This is used to play a game where the user must convert
    a series of base 10 numbers into base 2.

    It contains a single generateQuestions method to generate the series of questions
    """

    def generateQuestions(self):
        from random import randint
        score = 0

        for i in range(self.noOfQuestions):
            base10 = randint(1, 100)
            userResult = input("\n Please convert %d to binary: " % (base10))
            while True:
                try:
                    answer = int(userResult, base=2)
                    if answer == base10:
                        print("Correct Answer!")
                        score += 1
                        break
                    else:
                        print("Wrong answer. The correct answer is {:b}.".format(base10))
                        break
                except ValueError:
                    print("You did not enter a binary number. Please try again.")
                    userResult = input("\n Please convert %d to binary: " % (base10))

        return score


class MathGame(Game):
    """
    The MathGame class that inherits from our base Game class. This is used to play a game where the user must determine
    the answers to a series of mathematical expressions.

    It contains a single generateQuestions method to generate the series of questions
    """

    def generateQuestions(self):
        from random import randint
        score = 0
        numberList = [0, 0, 0, 0, 0]
        symbolList = ['', '', '', '']
        operatorDict = {1: '+', 2: '-', 3: '*', 4: '**'}

        for i in range(self.noOfQuestions):
            # populate the list of numbers with random integers between 1 and 9
            for index in range(0, 5):
                numberList[index] = randint(1, 9)

            '''
            populate the list of symbols with random operators from our dictionary
            
            make sure we don't have consecutive exponential operators since Python interprets this differently
            than a person would
            '''
            for index in range(0, 4):
                if index > 0 and symbolList[index - 1] == '**':
                    symbolList[index] = operatorDict[randint(1, 3)]
                else:
                    symbolList[index] = operatorDict[randint(1, 4)]

            # creates the question string that represents our full mathemtical expression
            questionString = str(numberList[0])
            for index in range(1, 4):
                questionString = questionString + symbolList[index] + str(numberList[index])

            # calls the eval function to have Python our mathematical expression string
            result = eval(questionString)

            # replaces ** with ^ to make it more human-readable
            questionString = questionString.replace("**", "^")

            '''
            asks the user for their answer and compares it with the one Python determined. if the answer is correct,
            then we add 1 to the user's score. otherwise, we display the correct answer. if the user did not enter
            a number, we ask them to try again.
            '''
            userResult = input("\nPlease evaluate %s: " % (questionString))
            while True:
                try:
                    answer = int(userResult)
                    if answer == result:
                        print("Correct Answer!")
                        score += 1
                        break
                    else:
                        print("Wrong answer. The correct answer is {:d}.".format(result))
                        break
                except ValueError:
                    print("You did not enter a valid number. Please try again.")
                    userResult = input("\nPlease evaluate %s: " % (questionString))

        return score
