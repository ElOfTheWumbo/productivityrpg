#!/bin/python

pwdFile = "PYPASS"
savFile  = "PYSAVE"

class playerInfo ( object ):
    def __init__ ( self ):
        health = 100
        energy = 100

def makeSave ( player ):
    db = open( savFile, "wb" )
    pickle.dump( player, db )

def loadSave ():
    db = open( savFile, "r" )
    return pickle.load( db )

def checkPass ( uInput ):
    db = open( pwdFile, "r" )
    password = db.read()

    if ( password == uInput ):
        return 0
    else:
        return 1

def setPass ( password ):
    db = open( pwdFile, "w" )
    db.write( password )
