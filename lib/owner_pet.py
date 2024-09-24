class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []  # Class variable to store all Pet instances

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"{pet_type} is not a valid pet type.")
        self.pet_type = pet_type
        self.owner = None
        
        if owner:
            self.set_owner(owner)

        Pet.all.append(self)  # Add the pet to the class variable all

    def set_owner(self, owner):
        """Sets the owner for the pet and adds the pet to the owner's list."""
        if not isinstance(owner, Owner):
            raise Exception("Owner must be an instance of the Owner class.")
        self.owner = owner
        owner.add_pet(self)


class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []  

    def pets(self):
        """Returns a list of the owner's pets."""
        return self._pets

    def add_pet(self, pet):
        """Adds a pet to the owner if it's a valid Pet instance."""
        if not isinstance(pet, Pet):
            raise Exception("The pet must be an instance of the Pet class.")
        
        pet.owner = self  
        self._pets.append(pet)

    def get_sorted_pets(self):
        """Returns a list of the owner's pets sorted by name."""
        return sorted(self._pets, key=lambda pet: pet.name)
