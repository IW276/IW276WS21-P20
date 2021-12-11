import getTensors
import database
import Person
import PxFeatureVector


class entry:

    tensors = getTensors.getTensors()
    db = database.database(-1, -1)
    print("Test")

    alltensors = tensors.getTensors()

    for tensor in alltensors:
        db.updatePersonByVector(tensor)
