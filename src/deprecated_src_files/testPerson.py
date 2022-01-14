import PxFeatureVector
import Person




class testPerson:
    def __init__(self):
        print("Test")
        self.testOnePerson()
        pass

    def run(self):
        print("test")
        self.testOnePerson()



    def testOnePerson(self):
        p = Person.Person(1)
        vector = PxFeatureVector.PxFeatureVector()
        print("1" + str(p.compareMeToPxVector(vector)))

print("tet")
t = testPerson()
t.testOnePerson()
