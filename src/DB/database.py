import Person


class database:
    allPersons = []
    lastUsedID = 0  # Actually used??
    threshhold = 2
    personTimeToLive = 5

    def __init__(self, newThreshhold, TTTForPersons):
        """Creates a database with the given threshholds.
        If none are given the parameters will be set as:
        threshhold for similarity: 0.9
        TimeToLiveForPersons (in frames): 5"""
        if newThreshhold > 0 & newThreshhold < 1:
            self.threshhold = newThreshhold

        if TTTForPersons > 0 & TTTForPersons < 9999:
            self.personTimeToLive = TTTForPersons

    def updatePersonByVector(self, newPxVector):
        bestRank = -1
        foundID = -1

        for compareWith in self.allPersons:
            newRank = compareWith.compareMeToPxVector(self, newPxVector)
            if newRank > bestRank:
                bestRank = newRank
                foundID = compareWith.getID()

        if bestRank > self.threshhold:
            self.allPersons[foundID].addPxVector(newPxVector)
            return foundID
        return -1

    def addPerson(self, newPerson):
        """First checks if this person already exists.
        If several existing persons match the best match (aka highest ranked)
        will be picked and updated with the vectors from newPerson.
        If no match was found a new person will be created and added.
        """
        oldID = self.__searchPerson(newPerson)

        if oldID < 0:
            nextID = self.__createNewID()
            newPerson.setID(nextID)
            self.allPersons.insert(nextID, newPerson)
            oldID = nextID
        else:
            personToUpdate = self.allPersons[oldID]
            personToUpdate.addPxVectors(self, newPerson.getPxVectors())

        return oldID

    def deletePersonByVector(self, pxVector):
        """Checks if a person's vectors are in average similar enough to the given vector
        to be declared as another vector of this person.
        If more exist, the closest (aka highest ranked) will be picked and deleted.
        """
        personToDelete = Person.Person(-1)
        personToDelete.addPxVector(pxVector)
        return self.deletePerson(personToDelete)

    def deletePerson(self, personToDelete):
        """Checks if a person is similar enough to the given person to be declared as the same.
        If more exist, the closest (aka highest ranked) will be picked and deleted.
        """
        id = self.__searchPerson(personToDelete)
        if id < 0:
            return id
        else:
            del self.allPersons[id]
            return id

        return -1

    def __createNewID(self):
        """Returns the next integer that is not in use as an ID."""
        nextID = 0

        for person in self.allPersons:
            if person.getID() == nextID:
                nextID += 1
        return nextID

    def __searchPerson(self, searchedPerson):
        """Searches for the given person, returns:
        The person's ID if one close enough to the given exists.
        -1 Otherwise.
        """

        bestRank = -1
        foundID = -1

        for compareWith in self.allPersons:
            newRank = compareWith.compareMeToPxVector(
                self, searchedPerson.getPxVectors()
            )
            if newRank > bestRank:
                bestRank = newRank
                foundID = compareWith.getID()

        if bestRank > self.threshhold:
            return foundID
        return -1

    def updateList(self):
        """Updates all persons, meaning every person that hasn't been detected since X frames, will be deleted."""

        for checkPerson in self.allPersons:
            age = checkPerson.getAge()
            if age > self.personTimeToLive:
                del self.allPersons[checkPerson.getID()]
