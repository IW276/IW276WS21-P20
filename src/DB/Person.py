

import collections
import PxFeatureVector

class Person:
    frames = collections.deque(maxlen=5)
    id = -1
    age = -1

    def __init__(self,myID):
        self.id = myID

    def getPxVector(self,num):
        return self.frames.index(num)

    def getPxVectors(self):
        return self.frames

    def addPxVector(self,newVector):
        if(0 == 0):
            pass #Implement checkup if newVector is a fitting vector!
        self.frames.append(newVector)
        age = 0
        return 1

    def addPxVectors(self,newVectors):
        for newVector in newVectors:
            self.addPxVector(newVector)

    def compareMeToPxVector(self,PxVector):
        averageRanking = 0
        amountOfFrames = 0

        for compareWith in self.frames:
            averageRanking += compareWith.comparePxVectors(compareWith)
            amountOfFrames += 1
        if(amountOfFrames == 0):
            return -1
        return (averageRanking / amountOfFrames)
        
    def getAge(self):
        return self.age

    def getID(self):
        return self.id
    
    def setID(self,myID):
        self.id = myID

