from hashlib import sha256
from os import listdir
from os import path

#variables
total = ''
debug = True#set this to False if you want everything to work properly
first_launch = False
folder = '../mixed/'

#arrays
files_sorted = [[],[],[]]
hash_sorted = []

#functions
def tots(files_sorted):
    number = 0
    for l1 in range(len(files_sorted)):
        for _ in range(len(files_sorted[l1])):
            number += 1
    return number

def any_to_sha256(files_sorted):
    with open(files_sorted, "rb") as f:
        hash = sha256()
        while chunk := f.read(8192):
            hash.update(chunk)
    out = hash.hexdigest()
    return out

def clean_sha256(hash_sorted):#untested
    #HASH_DUPES = [[],[],[]]
    hash_sorted_clean = [[],[],[]]
    for l1 in range(len(hash_sorted)):
        for l2 in range(len(hash_sorted[l1])):
            #HASH_DUPES[l1].append(hash_sorted[l1][l2])
            if hash_sorted[l1].count(hash_sorted[l1][l2]) > 1:
                #HASH_DUPES[l1].append(hash_sorted[l1][l2])
                hash_sorted[l1][l2] = '0'
            hash_sorted_clean[l1].append(hash_sorted[l1][l2])

    #print(str(HASH_DUPES))#temporary
    return hash_sorted_clean

def clean_sha256_with_base():#incomplete
    void()

#def create_db():
#    first_launch = True
#    conn = sqlite3.connect(base_name)
#    c = conn.cursor()
#    c.execute('CREATE TABLE files(sha256 text)')
#    c.execute('CREATE TABLE images(sha256 text)')
#    c.execute('CREATE TABLE videos(sha256 text)')
#    conn.commit()
#    conn.close()
#    return first_launch

def folder_to_list(folder):
    files_sorted[0] = listdir(folder+'files/')
    files_sorted[1] = listdir(folder+'photos/')
    files_sorted[2] = listdir(folder+'videos/')
    return files_sorted

def list_to_sha256(files_sorted,folder,total):
    hash_sorted = [[],[],[]]
    paths_sorted = [[],[],[]]
    progress = 0
    for l1 in range(len(files_sorted[0])):
        paths_sorted[0].append(folder+'files/'+files_sorted[0][l1])
    for l1 in range(len(files_sorted[1])):
        paths_sorted[1].append(folder+'photos/'+files_sorted[1][l1])
    for l1 in range(len(files_sorted[2])):
        paths_sorted[2].append(folder+'videos/'+files_sorted[2][l1])
    for l1 in range(len(paths_sorted)):
        for l2 in range(len(paths_sorted[l1])):
            hash_sorted[l1].append(any_to_sha256(paths_sorted[l1][l2]))
            progress += 1
            print("Hashed: " + str(progress) + " of " + str(total), end="\r")
    print('')
    return hash_sorted

def load_base_to_list(base_name): #TODO make
    base_list = [[],[],[]]
    #conn = sqlite3.connect(base_name)
    #c = conn.cursor()
    #c.execute('')
    #print(c.fetchall())
    return base_list

def merge_sha256_with_base(total):
    progress = 0
    #conn = sqlite3.connect(base_name)
    #c = conn.cursor()
    for l1 in range(len(hash_sorted[0])):
        params = hash_sorted[0][l1]
        #c.execute('INSERT INTO files VALUES(?)',(params,))
        progress += 1
        print("Stored: " + str(progress) + " of " + str(total), end="\r")
    for l1 in range(len(hash_sorted[1])):
        params = hash_sorted[1][l1]
        #c.execute('INSERT INTO images VALUES(?)',(params,))
        progress += 1
        print("Stored: " + str(progress) + " of " + str(total), end="\r")
    for l1 in range(len(hash_sorted[2])):
        params = hash_sorted[2][l1]
        #c.execute('INSERT INTO videos VALUES(?)',(params,))
        progress += 1
        print("Stored: " + str(progress) + " of " + str(total), end="\r")
    print('')
    #conn.commit()
    #conn.close()

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
#if not path.isfile(base_name):#If the database doesn't exists
#    first_launch = #create_db()#We create it and note that down

files_sorted = folder_to_list(folder)#Then the folder files get into the file list
if debug:
    files_sorted[0].clear()
    del files_sorted[1][1:-1]
    files_sorted[2].clear()
total = tots(files_sorted)#Then count all the files to display progress
hash_sorted = list_to_sha256(files_sorted,folder,total)#Then the file list gets converted to a sha256 list 
hash_sorted = clean_sha256(hash_sorted)#Then the sha256 list gets cleaned of duplicates
if not first_launch:
    #base_list = load_base_to_list(base_name)#Then database lists get loaded in
    ##clean_sha256_with_base()#Then database lists get compared to each of the representing groups of sha256 lists
    void()
total = tots(hash_sorted)
merge_sha256_with_base(total)#Then the cleaned sha256 list gets merged into the database
##move_dirty()#Then the last duplicate files get moved to DUPES folder
##move_clean()#Then remaining files get moved to the UPLOAD folder
###stats()#Then the statistics get displayed

#TODO add more progress visualization

#print(hash_sorted)#temporary
