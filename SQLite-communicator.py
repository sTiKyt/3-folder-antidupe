from hashlib import blake2b
from hashlib import sha256
from os import listdir
from os import path
import sqlite3

#variables
DB_NAME = 'sha256.sql'
FIRST_LAUNCH = False
FOLDER = '../mixed/'

#arrays
FILES_SORTED = [[],[],[]]
HASH_SORTED = []

#functions
def clean_dupe_list():#incomplete
    for l1 in HASH_SORTED[0]:
        print(l1)#temporary
    for l1 in HASH_SORTED[1]:
        print(l1)#temporary
    for l1 in HASH_SORTED[2]:
        print(l1)#temporary

def clean_sha256(HASH_SORTED):#incomplete
    HASH_SORTED_CLEAN = [[],[],[]]
    for l1 in range(len(HASH_SORTED[0])):
        HASH_SORTED_CLEAN[0].append(HASH_SORTED[0][l1])

    print(HASH_SORTED_CLEAN[0])#temporary
    return HASH_SORTED_CLEAN

def clean_sha256_with_db():#incomplete
    for l1 in HASH_SORTED[0]:
        print(l1)#temporary
    for l1 in HASH_SORTED[1]:
        print(l1)#temporary
    for l1 in HASH_SORTED[2]:
        print(l1)#temporary

def create_db():
    FIRST_LAUNCH = True
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''CREATE TABLE LIST([files] text, [photos] text, [videos] text)''')
    conn.commit()
    conn.close()
    return FIRST_LAUNCH

def dupes_to_dupe_list():#incomplete
    for l1 in HASH_SORTED[0]:
        print(l1)#temporary
    for l1 in HASH_SORTED[1]:
        print(l1)#temporary
    for l1 in HASH_SORTED[2]:
        print(l1)#temporary

def folder_to_list(FOLDER):
    FILES_SORTED[0] = listdir(FOLDER+'files/')
    FILES_SORTED[1] = listdir(FOLDER+'photos/')
    FILES_SORTED[2] = listdir(FOLDER+'videos/')
    return FILES_SORTED

def list_to_sha256(FILES_SORTED,FOLDER):#incomplete
    HASH_SORTED = [[],[],[]]
    PATHS_SORTED = [[],[],[]]
    for l1 in range(len(FILES_SORTED[0])):
        PATHS_SORTED[0].append(FOLDER+'files/'+FILES_SORTED[0][l1])
    for l1 in range(len(FILES_SORTED[1])):
        PATHS_SORTED[1].append(FOLDER+'photos/'+FILES_SORTED[1][l1])
    for l1 in range(len(FILES_SORTED[2])):
        PATHS_SORTED[2].append(FOLDER+'videos/'+FILES_SORTED[2][l1])
    
    for l1 in range(len(PATHS_SORTED)):
        for l2 in range(len(PATHS_SORTED[l1])):
            with open(PATHS_SORTED[l1][l2], 'rb') as file:
                #TEMP = str(file.read())
                HASH_SORTED[l1].append(sha256(file.read()).hexdigest())
            
    print(HASH_SORTED[0][0])#temporary
    
#    for l1 in range(len(PATHS_SORTED)):
#        for l2 in range(len(PATHS_SORTED[l1])):
#            HASH_SORTED[l1].append(sha256(PATHS_SORTED[l1][l2].encode('utf-8')).hexdigest())
    return HASH_SORTED

def load_db_to_list(): #TODO make
    void()

def merge_sha256_with_db():#incomplete
    for l1 in HASH_SORTED[0]:
        print(l1)#temporary
    for l1 in HASH_SORTED[1]:
        print(l1)#temporary
    for l1 in HASH_SORTED[2]:
        print(l1)#temporary

def move_clean():#incomplete
    for l1 in HASH_SORTED[0]:
        print(l1)#temporary
    for l1 in HASH_SORTED[1]:
        print(l1)#temporary
    for l1 in HASH_SORTED[2]:
        print(l1)#temporary

def move_dirty():#incomplete
    for l1 in HASH_SORTED[0]:
        print(l1)#temporary
    for l1 in HASH_SORTED[1]:
        print(l1)#temporary
    for l1 in HASH_SORTED[2]:
        print(l1)#temporary

def stats(): #TODO make
    void()

#THE ALMIGHTY VOID
def void():
    return

#main
if not path.isfile(DB_NAME):#If the database doesn't exists
    FIRST_LAUNCH = create_db()#We create it and note that down

FILES_SORTED = folder_to_list(FOLDER)#Then the folder files get into the file list
HASH_SORTED = list_to_sha256(FILES_SORTED,FOLDER)#Then the file list gets converted to a sha256 list
#HASH_SORTED = clean_sha256(HASH_SORTED)#Then the sha256 list gets cleaned of duplicates
#dupes_to_dupe_list()#Then the duplicated files get into a dupe list
#move_dirty()#Then duplicates are being moved to a DUPES folder
#clean_dupe_list()#Then the dupe list gets removed
if not FIRST_LAUNCH:
    #load_db_to_list()#Then database lists get loaded in
    #clean_sha256_with_db()#Then database lists get compared to each of the representing groups of sha256 lists
    void()
#merge_sha256_with_db()#Then the cleaned sha256 list gets merged into the database
#move_dirty()#Then the last duplicate files get moved to DUPES folder
#clean_dupe_list()#Then the dupe list gets removed
#move_clean()#Then remaining files get moved to the UPLOAD folder
#stats()#Then the statistics get displayed

#TODO add progress visualization

#print(HASH_SORTED)#temporary
