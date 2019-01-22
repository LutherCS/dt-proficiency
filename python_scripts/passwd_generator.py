#!/usr/bin/env python3
"""Generate a pseudo passwd file"""

import random

shells = [
    "/usr/sbin/nologin",
    "/bin/false",
    "/bin/bash",
    "/bin/csh",
    "/bin/ksh",
    "/bin/zsh",
]

uid_set = set()

with open("roster.txt", "r") as input_file:
    for line in input_file:
        name_lst = line.strip().split(", ")
        name = name_lst[1] + " " + name_lst[0]
        uname = name_lst[0][:4] + name_lst[1][:2] + "0" + str(random.randint(1, 9))
        uname = uname.lower()
        uid = random.randint(1000, 1100)
        while uid in uid_set:
            uid = random.randint(1000, 1100)
        uid_set.add(uid)
        gid = uid
        print(
            "{}:{}:{}:{}:{},,,:{}:{}".format(
                uname, "x", uid, gid, name, "/home/" + uname, random.choice(shells)
            )
        )
