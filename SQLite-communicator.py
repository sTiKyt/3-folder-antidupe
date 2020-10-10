from hashlib import sha256
from os import listdir, mkdir, path, rename

#variables
base_name = 'mixed'
total = ''
debug = False
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

def clean_sha256(hash_sorted):
    hash_sorted_clean = [[],[],[]]
    for l1 in range(len(hash_sorted)):
        for l2 in range(len(hash_sorted[l1])):
            if hash_sorted[l1].count(hash_sorted[l1][l2]) > 1:
                hash_sorted[l1][l2] = '0'
            hash_sorted_clean[l1].append(hash_sorted[l1][l2])
    return hash_sorted_clean

def clean_sha256_with_base(base_list,hash_sorted):
    progress = 0
    for l1 in range(len(hash_sorted[0])):
        if hash_sorted[0][l1] in base_list[0]:
            progress += 1
            print("Duplicates: " + str(progress) + " out of " + str(total), end="\r")
            hash_sorted[0][l1] = '0'
    for l1 in range(len(hash_sorted[1])):
        if hash_sorted[1][l1] in base_list[1]:
            progress += 1
            print("Duplicates: " + str(progress) + " out of " + str(total), end="\r")
            hash_sorted[1][l1] = '0'
    for l1 in range(len(hash_sorted[2])):
        if hash_sorted[2][l1] in base_list[2]:
            progress += 1
            print("Duplicates: " + str(progress) + " out of " + str(total), end="\r")
            hash_sorted[2][l1] = '0'
    if progress == 0:
        print('No duplicates found!                ')#16 "spaces" give enough room for masking the symbols written before
    if progress == total:
        print('There is not a single new file.     ')
    else:
        print('')
    hash_sorted_out = hash_sorted
    return hash_sorted_out

def create_base():
    first_launch = True
    mkdir(base_name)
    return first_launch

def folder_to_list(folder):
    files_sorted[0] = listdir(folder+'files/')
    files_sorted[1] = listdir(folder+'photos/')
    files_sorted[2] = listdir(folder+'videos/')
    return files_sorted

def list_to_sha256(files_sorted,folder,total):
    hash_sorted = [[],[],[]]
    paths_sorted = [[],[],[]]
    progress = 0
    workfolder = folder+'files/'
    for l1 in range(len(files_sorted[0])):
        paths_sorted[0].append(workfolder+files_sorted[0][l1])
    workfolder = folder+'photos/'
    for l1 in range(len(files_sorted[1])):
        paths_sorted[1].append(workfolder+files_sorted[1][l1])
    workfolder = folder+'videos/'
    for l1 in range(len(files_sorted[2])):
        paths_sorted[2].append(workfolder+files_sorted[2][l1])
    for l1 in range(len(paths_sorted)):
        for l2 in range(len(paths_sorted[l1])):
            with open(paths_sorted[l1][l2], "rb") as f:
                hash = sha256()
                while chunk := f.read(8192):
                    hash.update(chunk)
            hash_sorted[l1].append(hash.hexdigest())
            progress += 1
            print("Hashed: " + str(progress) + " of " + str(total), end="\r")
    print('')
    return hash_sorted

def load_base_to_list(base_name):
    base_list = [[],[],[]]
    with open(base_name+'/files', 'r') as f:
        for line in f.readlines():
            base_list[0].append(line.strip())
    with open(base_name+'/photos', 'r') as f:
        for line in f.readlines():
            base_list[1].append(line.strip())
    with open(base_name+'/videos', 'r') as f:
        for line in f.readlines():
            base_list[2].append(line.strip())
    return base_list

def merge_sha256_with_base(total):
    progress = 0
    with open(base_name+'/files', 'a') as f:
        for l1 in range(len(hash_sorted[0])):
            if not hash_sorted[0][l1] == '0':
                f.write(hash_sorted[0][l1]+'\n')
                progress += 1
                print("Stored: " + str(progress) + " of " + str(total), end="\r")
    with open(base_name+'/photos', 'a') as f:
        for l1 in range(len(hash_sorted[1])):
            if not hash_sorted[1][l1] == '0':
                f.write(hash_sorted[1][l1]+'\n')
                progress += 1
                print("Stored: " + str(progress) + " of " + str(total), end="\r")
    with open(base_name+'/videos', 'a') as f:
        for l1 in range(len(hash_sorted[2])):
            if not hash_sorted[2][l1] == '0':
                f.write(hash_sorted[2][l1]+'\n')
                progress += 1
                print("Stored: " + str(progress) + " of " + str(total), end="\r")
    if progress == 0:
        print('Nothing to merge!')
    else:
        print('')

def move_clean(folder):
    folder = folder[:-1]
    rename(folder,folder+'_clean')

def move_dirty():
    if not path.exists(folder+'../dupes/'):
        mkdir(folder+'../dupes/')
    dupes = folder+'../dupes/'
    for l1 in range(len(hash_sorted)):
        if not hash_sorted[l1].count('0') == 0:
            for l2 in range(len(hash_sorted[l1])):
                if hash_sorted[l1][l2] == '0':
                    sf = 'files/'
                    if l1 == 1:
                        sf = 'photos/'
                    if l1 == 2:
                        sf = 'videos/'
                    if not path.exists(folder+'../dupes/'+sf):
                        mkdir(folder+'../dupes/'+sf)
                    rename(folder+sf+files_sorted[l1][l2],dupes+sf+files_sorted[l1][l2])


#def stats(): #TODO make
#    void()

#THE ALMIGHTY VOID
#def void():
#    return

#main
if not path.exists(base_name):#If the database doesn't exists
    first_launch = create_base()#We create it and note that down
files_sorted = folder_to_list(folder)#Then the folder files get into the file list
if debug:
    del files_sorted[0][0:-1]
    del files_sorted[1][0:-1]
    del files_sorted[2][0:-1]
total = tots(files_sorted)#Then count all the files to display progress
hash_sorted = list_to_sha256(files_sorted,folder,total)#Then the file list gets converted to a sha256 list
hash_sorted = clean_sha256(hash_sorted)#Then the sha256 list gets cleaned of duplicates
if not first_launch:
    base_list = load_base_to_list(base_name)#Then database lists get loaded in
    hash_sorted = clean_sha256_with_base(base_list,hash_sorted)#Then database lists get compared to each of the representing groups of sha256 lists
total = tots(hash_sorted)
merge_sha256_with_base(total)#Then the cleaned sha256 list gets merged into the database
move_dirty()#Then the last duplicate files get moved to DUPES folder
move_clean(folder)#Then remaining files get moved to the UPLOAD folder
###stats()#Then the statistics get displayed

#TODO add more progress visualization

#print(hash_sorted)#temporary
