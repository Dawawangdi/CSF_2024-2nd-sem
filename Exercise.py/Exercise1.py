std_list = []
std_dict={}

std_list.append ('karma')
std_dict ['karma'] = {'18' and '12'}
std_list.append ('dorji')
std_dict['dorji'] ={ '18'and '12'}

name = input('Enter the name: ')
age = input('Enter the age: ')
grade = input ('Enter the Grade: ')
std_list.append(name)
std_dict[name] = {'Age': age,'grade':grade}
print("Student added successfully")

print("Student Details:\n ")
for std in std_list:
    print(std)

#search

search_name = print("Enter the student name you want to search for: ")
if search_name in std_list:
    print(f"Student name found:\n Age: {std_dict[std_list]},\n Grade: {std_dict[std_list]}")
else:
    print("Sorry, no name found")



#remove name
remove_name = print("enter the name you want to remove: ")
if remove_name in std_list:
    remove_details = std_dict[remove_name]
    std_list.remove(remove_name)
    std_dict.pop(remove_details)
    del std_dict[remove_name]
    print("student removed successfully")
else:
    print("student not found")
















