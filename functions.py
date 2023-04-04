
## FILEPATH = "todos.txt"
#
# abcd.txt get_todos(filepath=FILEPATH):
#     with open(filepath, 'r') as file_local:
#         todos_local = file_local.readlines()
#     return todos_local
#
#
# abcd.txt write_todos(todos_arg, filepath=FILEPATH):
#     with open('filepath', 'w') as file:
#         file.writelines(todos_arg)

#
# import glob
#
# myfiles = glob.glob("modules/*.txt")
#
# for filepath in myfiles:
#     with open(filepath, 'r') as file:
#         print(file.read().upper())
FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

if __name__ == "__main__":
    print("Helllo")
    print(get_todos())
