import getTensors
import database
import Person
import PxFeatureVector


class entry:

    tensors = getTensors.getTensors()
    db = database.database(-1, -1)  # Gute Werte???
    print("Test")

    alltensors = tensors.getTensors()

    for tensor in alltensors:
        db.update_person_by_vector(tensor)
