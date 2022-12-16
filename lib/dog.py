#!/usr/bin/env python3

class Dog:

    breeds = ["mastif", "chihuahua", "corgi", "shar pei", "beagle", "french bulldog", "pug", "Pointer"]

    def get_name(self):
        return self._name

    def set_name(self, name):
        if type(name) == str and 1 <= len(name) <= 25:
                self._name = name
        else:
            print("Name must be string between 1 and 25 characters.")
    
    def get_breed(self):
        return self._breed

    def set_breed(self, breed):
        if breed.lower() not in Dog.breeds:
            print("Breed must be in list of approved breeds.")
        else:
            self._breed = breed
            
    
    name = property(get_name, set_name,)
    breed = property(get_breed, set_breed,)

