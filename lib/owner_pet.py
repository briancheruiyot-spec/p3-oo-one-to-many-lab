class Pet:
    # Class variable to store valid pet types
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    # Class variable to store all instances of the Pet class
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        # Validate pet_type
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type. Valid types are: {', '.join(Pet.PET_TYPES)}")
        self.pet_type = pet_type
        self.owner = owner
        
        # Add this pet to the global list of pets
        Pet.all.append(self)
        
        # If owner is provided, add this pet to their list
        if isinstance(owner, Owner):
            owner.add_pet(self)


class Owner:
    def __init__(self, name):
        self.name = name
    
    def pets(self):
        # Return all pets owned by this owner
        return [pet for pet in Pet.all if isinstance(pet, Pet) and pet.owner == self]
    
    def add_pet(self, pet):
        # Check if the pet is an instance of the Pet class
        if not isinstance(pet, Pet):
            raise Exception("The pet must be an instance of the Pet class.")
        # Add the pet to the owner's list
        pet.owner = self

    def get_sorted_pets(self):
        # Get all pets of the owner and sort them by name
        pets_of_owner = self.pets()
        return sorted(pets_of_owner, key=lambda pet: pet.name)


# Example usage
try:
    owner1 = Owner("Alice")
    pet1 = Pet("Buddy", "dog", owner1)
    pet2 = Pet("Whiskers", "cat", owner1)

    owner2 = Owner("Bob")
    pet3 = Pet("Rex", "dog", owner2)

    # Test the methods
    print(f"Alice's pets: {[pet.name for pet in owner1.get_sorted_pets()]}")
    print(f"Bob's pets: {[pet.name for pet in owner2.get_sorted_pets()]}")
except Exception as e:
    print(e)
