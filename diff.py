import re
from collections import defaultdict


def compare_files(f1, f2):
    # opens the new file and reads/stores lines in list1
    list1 = open(f1, "r").readlines()
    # opens the new file and reads/stores lines in list2
    list2 = open(f2, "r").readlines()
    d1 = defaultdict(list)
    d2 = defaultdict(list)
    # create a dictionary where the lines in the lists are seperated by a " " for their key/value pairs
    for item in list1:
        k = item[:40]
        v = item[41:]
        # print(k)
        d1[k].append(v)

    for item in list2:
        k = item[:40]
        v = item[41:]
        # print(k)
        d2[k].append(v)

    for k in d1:
        # print(d1[k])
        print(k)
        if d1[k] == d2[k]:
            del d2[k]
    # rejoin the key/value pairs back into prior format and write it to an output file.
    if user_input != 1:
        with open("NewNotInOld.txt", "w") as output:
            output.writelines(
                ["{} {}".format(k, d2[k][0]) for k in d2 if len(d2[k]) == 1]
            )
    else:
        with open("OldNotInNew.txt", "w") as output:
            output.writelines(
                ["{} {}".format(k, d2[k][0]) for k in d2 if len(d2[k]) == 1]
            )


# def diff_new_to_old(f1, f2):
#     # opens the new file and reads/stores lines in list1
#     list1 = open(f1, "r").readlines()
#     # opens the new file and reads/stores lines in list2
#     list2 = open(f2, "r").readlines()
#     d1 = defaultdict(list)
#     d2 = defaultdict(list)
#     # create a dictionary where the lines in the lists are seperated by a " " for their key/value pairs
#     for item in list1:
#         k, v = item.split(" ")
#         d1[k].append(v)

#     for item in list2:
#         k, v = item.split(" ")
#         d2[k].append(v)

#     for k in d1:
#         if k in d1 and (d1[k] == d2[k]):
#             del d2[k]
#     # rejoin the key/value pairs back into prior format and write it to an output file.
#     with open("NewNotInOld.txt", "w") as output:
#         output.writelines(["{} {}".format(k, d2[k][0]) for k in d2 if len(d2[k]) == 1])


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
