import Person



class database:
    allPersons = []
    lastUsedID = 0 #Actually used??
    threshhold = 1

    def __init__(self,newThreshhold):
        if(newThreshhold < 0 | newThreshhold > 1):
            self.threshhold = 0.9
        else:
            self.threshhold = newThreshhold
        

    def updatePerson(self,newPxVector):
        bestRank = -1
        foundID = -1

        for compareWith in self.allPersons:
            newRank = compareWith.compareMeToPxVector(self,newPxVector)
            if(newRank > bestRank):
                bestRank = newRank
                foundID = compareWith.getID()

        if(bestRank > self.threshhold):
            self.allPersons[foundID].addPxVector(newPxVector)
            return foundID
        return -1


    def addPerson(self,newPerson):
        oldID = self.searchPerson(newPerson)

        if(oldID < 0):
            nextID = self.createNewID()
            newPerson.setID(nextID)
            self.allPersons.insert(nextID,newPerson)
            oldID = nextID
        else:           
            personToUpdate = self.allPersons[oldID]
            personToUpdate.addPxVectors(self,newPerson.getPxVectors())

        return oldID

    def deletePersonByVector(self,pxVector):
        personToDelete = Person.Person(-1)
        personToDelete.addPxVector(pxVector)
        return self.deletePerson(personToDelete)

    def deletePerson(self,personToDelete):
        id = self.searchPerson(personToDelete)
        if(id < 0):
            return id
        else:
            del self.allPersons[id]
            return id

        return -1

    def createNewID(self):
        nextID = 0

        for person in self.allPersons:
            if(person.getID() == nextID):
                nextID += 1
        return nextID


    def searchPerson(self, searchedPerson):
        
        bestRank = -1
        foundID = -1

        for compareWith in self.allPersons:
            newRank = compareWith.compareMeToPxVector(self,searchedPerson.getPxVectors())
            if(newRank > bestRank):
                bestRank = newRank
                foundID = compareWith.getID()

        if(bestRank > self.threshhold):
            return foundID
        return -1