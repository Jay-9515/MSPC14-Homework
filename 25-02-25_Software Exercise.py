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