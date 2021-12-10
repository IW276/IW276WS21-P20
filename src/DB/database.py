import Person


class database:
    all_persons = []
    last_used_i_d = 0  # actually used??
    threshhold = 2
    person_time_to_live = 5

    def __init__(self, new_threshhold, time_to_live_for_persons):
        """Creates a database with the given threshholds.
        If none are given the parameters will be set as:
        threshhold for similarity: 0.9
        TimeToLiveForPersons (in frames): 5"""
        if new_threshhold > 0 & new_threshhold < 1:
            self.threshhold = new_threshhold

        if time_to_live_for_persons > 0 & time_to_live_for_persons < 9999:
            self.person_time_to_live = time_to_live_for_persons

    def update_person_by_vector(self, new_px_vector):
        best_rank = -1
        found_i_d = -1

        for compare_with in self.all_persons:
            if compare_with.get_age != 0:
                new_rank = compare_with.compare_me_to_px_vector(self, new_px_vector)
                if new_rank > best_rank:
                    best_rank = new_rank
                    found_i_d = compare_with.get_i_d()

        if best_rank > self.threshhold:
            self.all_persons[found_i_d].add_px_vector(new_px_vector)
            return found_i_d
        else:
            new_person = _person._person(self.__create_new_i_d)
            self.all_persons.append(new_person)
        return -1

    def add_person(self, new_person):
        """First checks if this person already exists.
        If several existing persons match the best match (aka highest ranked)
        will be picked and updated with the vectors from newPerson.
        If no match was found a new person will be created and added.
        """
        oldID = self.__search_person(new_person)

        if oldID < 0:
            next_i_d = self.__create_new_i_d()
            new_person.set_i_d(next_i_d)
            self.all_persons.insert(next_i_d, new_person)
            oldID = next_i_d
        else:
            person_to_update = self.all_persons[oldID]
            person_to_update.add_px_vectors(self, new_person.get_px_vectors())

        return oldID

    def delete_person_by_vector(self, px_vector):
        """Checks if a person is similar enough to the given person to be declared as the same.
        If more exist, the closest (aka highest ranked) will be picked and deleted.
        """

        person_to_delete = _person._person(-1)
        person_to_delete.add_px_vector(px_vector)
        return self.delete_person(person_to_delete)

    def delete_person(self, person_to_delete):
        """Checks if a person's vectors are in average similar enough to the given vector
        to be declared as another vector of this person.
        If more exist, the closest (aka highest ranked) will be picked and deleted.
        """
        id = self.__search_person(person_to_delete)
        if id < 0:
            return id
        else:
            del self.all_persons[id]
            return id

        return -1

    def __create_new_i_d(self):
        """Returns the next integer that is not in use as an ID."""
        next_i_d = 0

        for person in self.all_persons:
            if person.get_i_d() == next_i_d:
                next_i_d += 1
        return next_i_d

    def __search_person(self, searched_person):
        """Searches for the given person, returns:
        The person's ID if one close enough to the given exists.
        -1 Otherwise.
        """

        best_rank = -1
        found_i_d = -1

        for compare_with in self.all_persons:
            new_rank = compare_with.compare_me_to_px_vector(
                self, searched_person.get_px_vectors()
            )
            if new_rank > best_rank:
                best_rank = new_rank
                found_i_d = compare_with.get_i_d()

        if best_rank > self.threshhold:
            return found_i_d
        return -1

    def update_list(self):
        """Updates all persons, meaning every person that hasn't been detected since X frames, will be deleted."""

        for check_person in self.all_persons:
            age = check_person.get_age()
            if age > self.person_time_to_live:
                del self.all_persons[check_person.get_i_d()]
