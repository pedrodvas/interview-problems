size = 100

char_list = ["[", "]"]

for i in range(size):
    char_list.insert(len(char_list)-2, str(i)+", ")

char_list.insert(0, "[")
char_list.pop(len(char_list)-2)

string = "".join(char_list)

print(string)