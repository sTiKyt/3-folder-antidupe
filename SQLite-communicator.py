from hashlib import blake2b
from hashlib import sha256
from os import listdir
from os import path
import sqlite3

#variables
ALL = ''
DB_NAME = 'sha256.sql'
DEBUG = True#set this to False if you want everything to work properly
FIRST_LAUNCH = False
FOLDER = '../mixed/'

#arrays
FILES_SORTED = [[],[],[]]
HASH_SORTED = []

#functions
def total(FILES_SORTED):
    NUMBER = 0
    for l1 in range(len(FILES_SORTED)):
        for _ in range(len(FILES_SORTED[l1])):
            NUMBER += 1
    return NUMBER

def any_to_sha256(FILES_SORTED):
    with open(FILES_SORTED, "rb") as FILE:
        HASH = sha256()
        while CHUNK := FILE.read(8192):
            HASH.update(CHUNK)
    OUT = HASH.hexdigest()
    return OUT

def clean_sha256(HASH_SORTED):#untested
    #HASH_DUPES = [[],[],[]]
    HASH_SORTED_CLEAN = [[],[],[]]
    for l1 in range(len(HASH_SORTED)):
        for l2 in range(len(HASH_SORTED[l1])):
            #HASH_DUPES[l1].append(HASH_SORTED[l1][l2])
            if HASH_SORTED[l1].count(HASH_SORTED[l1][l2]) > 1:
                #HASH_DUPES[l1].append(HASH_SORTED[l1][l2])
                HASH_SORTED[l1][l2] = '0'
            HASH_SORTED_CLEAN[l1].append(HASH_SORTED[l1][l2])

    #print(str(HASH_DUPES))#temporary
    return HASH_SORTED_CLEAN

def clean_sha256_with_db():#incomplete
    void()

def create_db():
    FIRST_LAUNCH = True
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('CREATE TABLE files(sha256 text)')
    c.execute('CREATE TABLE images(sha256 text)')
    c.execute('CREATE TABLE videos(sha256 text)')
    conn.commit()
    conn.close()
    return FIRST_LAUNCH

def folder_to_list(FOLDER):
    FILES_SORTED[0] = listdir(FOLDER+'files/')
    FILES_SORTED[1] = listdir(FOLDER+'photos/')
    FILES_SORTED[2] = listdir(FOLDER+'videos/')
    return FILES_SORTED

def list_to_sha256(FILES_SORTED,FOLDER,ALL):
    HASH_SORTED = [[],[],[]]
    PATHS_SORTED = [[],[],[]]
    PROGRESS = 0
    for l1 in range(len(FILES_SORTED[0])):
        PATHS_SORTED[0].append(FOLDER+'files/'+FILES_SORTED[0][l1])
    for l1 in range(len(FILES_SORTED[1])):
        PATHS_SORTED[1].append(FOLDER+'photos/'+FILES_SORTED[1][l1])
    for l1 in range(len(FILES_SORTED[2])):
        PATHS_SORTED[2].append(FOLDER+'videos/'+FILES_SORTED[2][l1])
    for l1 in range(len(PATHS_SORTED)):
        for l2 in range(len(PATHS_SORTED[l1])):
            HASH_SORTED[l1].append(any_to_sha256(PATHS_SORTED[l1][l2]))
            PROGRESS += 1
            print("Hashed: " + str(PROGRESS) + " of " + str(ALL), end="\r")
    print('')
    return HASH_SORTED

def load_db_to_list(): #TODO make
    void()

def merge_sha256_with_db(ALL):
    PROGRESS = 0
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    for l1 in range(len(HASH_SORTED[0])):
        params = HASH_SORTED[0][l1]
        c.execute('INSERT INTO files VALUES(?)',(params,))
        PROGRESS += 1
        print("Stored: " + str(PROGRESS) + " of " + str(ALL), end="\r")
    for l1 in range(len(HASH_SORTED[1])):
        params = HASH_SORTED[1][l1]
        c.execute('INSERT INTO images VALUES(?)',(params,))
        PROGRESS += 1
        print("Stored: " + str(PROGRESS) + " of " + str(ALL), end="\r")
    for l1 in range(len(HASH_SORTED[2])):
        params = HASH_SORTED[2][l1]
        c.execute('INSERT INTO videos VALUES(?)',(params,))
        PROGRESS += 1
        print("Stored: " + str(PROGRESS) + " of " + str(ALL), end="\r")
    print('')
    conn.commit()
    conn.close()

def move_clean():#incomplete
    void()

def move_dirty():#incomplete
    void()

def stats(): #TODO make
    void()

#THE ALMIGHTY VOID
def void():
    return

#main
if not path.isfile(DB_NAME):#If the database doesn't exists
    FIRST_LAUNCH = create_db()#We create it and note that down

FILES_SORTED = folder_to_list(FOLDER)#Then the folder files get into the file list
if DEBUG:
    FILES_SORTED[0].clear()
    del FILES_SORTED[1][1:-1]
    FILES_SORTED[2].clear()
ALL = total(FILES_SORTED)#Then count all the files to display progress
HASH_SORTED = list_to_sha256(FILES_SORTED,FOLDER,ALL)#Then the file list gets converted to a sha256 list 
HASH_SORTED = clean_sha256(HASH_SORTED)#Then the sha256 list gets cleaned of duplicates
if not FIRST_LAUNCH:
    ##load_db_to_list()#Then database lists get loaded in
    ##clean_sha256_with_db()#Then database lists get compared to each of the representing groups of sha256 lists
    void()
ALL = total(HASH_SORTED)
merge_sha256_with_db(ALL)#Then the cleaned sha256 list gets merged into the database
##move_dirty()#Then the last duplicate files get moved to DUPES folder
##move_clean()#Then remaining files get moved to the UPLOAD folder
###stats()#Then the statistics get displayed

#TODO add more progress visualization

#print(HASH_SORTED)#temporary
