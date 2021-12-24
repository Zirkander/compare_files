from collections import defaultdict


def compare_files(f1, f2):
    # opens the new file and reads/stores lines in list1
    list1 = open(f1, "r").readlines()
    # opens the new file and reads/stores lines in list2
    list2 = open(f2, "r").readlines()

    # create 2 dictionaries where the lines in the lists are seperated by their hash as the keys and filenames as the values.
    d1 = defaultdict(list)
    d2 = defaultdict(list)

    #Read the first file and take the first 40 characters and put them into a key, add the rest of the characters to the value, do this for both dictionaries.
    for item in list1:
        k = str(item[:40])
        v = str(item[41:])
        # print(k)
        d1[k].append(v)

    for item in list2:
        k = str(item[:40])
        v = str(item[41:])
        # print(k)
        d2[k].append(v)
    
    #Retrieve dictionary1 keys and then check them against dictionary2. If keys are in both, then remove that key/value pair from the dictionary.
    for k in list(d1):
        if k in d2.keys():
            d2.pop(k)
    # rejoin the key/value pairs back into proper format and output the text to a seperate file depending on the users choice.
    if user_input != 1:
        with open("NewNotInOld.txt", "w") as output:
            output.writelines(["{}".format(d2[k][0]) for k in d2 if len(d2[k]) == 1])
    else:
        with open("OldNotInNew.txt", "w") as output:
            output.writelines(["{}".format(d2[k][0]) for k in d2 if len(d2[k]) == 1])


print("What would you like to do?")
print("Please press 1 if you would like to retreive what is not in the new files")
print("Please press 2 if you would like to retreive what is not in the old files")
user_input = int(input("What would you like to do?: "))
print(user_input)
if user_input == 1:
    compare_files(
        input("What is the new file: "),
        input("What is the old file for comparison: "),
    )
elif user_input == 2:
    compare_files(
        input("What is the old file: "),
        input("What is the new file for comparison: "),
    )
else:
    print("Please choose 1 or 2")
