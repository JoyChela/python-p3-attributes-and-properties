#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name="Buddy", breed="Mastiff"):
        self._name = None
        self._breed = None

        self.name = name  # Use the public property setter
        self.breed = breed  # Use the public property setter

    def _validate_name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 25:
            return name
        else:
            print("Name must be string between 1 and 25 characters.")
            return None

    def _validate_breed(self, breed):
        if breed in APPROVED_BREEDS:
            return breed
        else:
            print("Breed must be in list of approved breeds.")
            return None

    # Public getter and setter for name
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        validated_name = self._validate_name(name)
        if validated_name is not None:
            self._name = validated_name

    # Public getter and setter for breed
    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, breed):
        validated_breed = self._validate_breed(breed)
        if validated_breed is not None:
            self._breed = validated_breed