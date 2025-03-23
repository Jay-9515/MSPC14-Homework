# -*- coding: utf-8 -*-
"""
Created on Sun Mar 23 10:35:18 2025

@author: JAY
"""

message = "https://database.com/user/augustom,AugUSto Martin, 23, Approved,,"
message = "https://database.com/user/juliasch,JuLIA SchmidT, 67, rejected,,"
message = "https://database.com/user/kmarx,Karl Marx, 42, rejected,,"

# Complete the code

def revised_message(message):

    message = message.replace("https://database.com/user/","")

    parts = message.split(",")

    First = parts[0].strip().lower()
    Last = parts[1].strip().lower()
    age = parts[3].strip()
    status = parts[4].strip()

    revised_message = f"message: {First},{Last},{age},{status}"

    return revised_message

message  = "https://database.com/user/augustom,AugUSto Martin, 23, Approved,,"
print(revised_message(message))


def arc_length(angle,D):
    pi = 3.14;
    result = (pi/180)*angle*(diameter/2);
    return f"arc_length is: {result}"
    
angle = 45
diameter = 9

print(arc_length(angle,diameter))