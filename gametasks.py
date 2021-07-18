def printInstructions(instruction):
    """
    Prints the given instruction
    """
    print(instruction)


def getUserScore(userName):
    """
    Searches the userScores.txt file for the given userName and returns either the corresponding score or -1
    """
    try:
        file = open('userScores.txt', 'r')
        for line in file:
            content = line.split(', ')
            if content[0] == userName:
                file.close()
                return content[1]
            file.close()
            return '-1'
    except IOError:
        print("File not found. A new file will be created.")
        file = open('userScores.txt', 'w')
        file.close()
        return '-1'


def updateUserScore(newUser, userName, score):
    """
    Updates a user's score by copying all scores from the userScores.txt file into a userScores.tmp file, changing
    the specific user's score that needs to be updated, deleting the old userScores.txt file and renaming the
    userScores.tmp file to userScores.txt.
    """
    from os import remove, rename

    if newUser:
        file = open('userScores.txt', 'a')
        file.write(userName + ', ' + score + '\n')
        file.close()
    else:
        tmpFile = open('userScores.tmp', 'w')
        file = open('userScores.txt', 'r')

        for line in file:
            content = line.split(', ')
            if content[0] == userName:
                tmpFile.write(userName + ',' + score + '\n')
            else:
                tmpFile.write(line)

        file.close()
        tmpFile.close()

        remove('userScores.txt')
        rename('userScores.tmp', 'userScores.txt')
