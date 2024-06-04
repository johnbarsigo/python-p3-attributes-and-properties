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
    
    def __init__( self, breed = "Mastiff" , name = "Rex" ):
        if ( type (name) == str ) and ( 1 <= len(name) <= 25 ) :
            # print ( "Saving name" )
            self.name = name

            if breed in APPROVED_BREEDS :
                # print ( "Registering breed" )
                self.breed = breed
            else :
                print ( "Breed must be in list of approved breeds." )

        else :
            print ( "Name must be string between 1 and 25 characters." )
        

snoop = Dog ( "K-9", "Snoop" )
