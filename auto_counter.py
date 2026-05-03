path_to_file = "/home/zak-holmes/Vault/Brain/"

file_name = "Apriltest.md"

# things for this to do
#     - Count all the sub totals (start with $, end with = )
#     - Count the categries (every number inbetween headings / #)

# Minor improvments - proper functions 

def sub_totals(file_path):

    with open (file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    modified_lines = []
    for line in lines:
        dollar_index = line.find("$")
        equals_index = line.find("=")
        if dollar_index != -1 and equals_index != -1:
            amount_sub = line[dollar_index + 1:equals_index].split("+")
            total = 0
            for amount in amount_sub:
                total += float(amount.strip())
            new_line = f"{line.rstrip("\n")} {total:.2f}\n"
            print(new_line)
            modified_lines.append(new_line)
        else:
            modified_lines.append(line)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(modified_lines)

#
def count_categories(file_path):
    with open (file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    current_cat_index = None
    for line in lines:
        cat_index = line.find("##")
        equals_index = line.find("=")
        if cat_index != -1 or lines.index(line) == len(lines)-1: #If at a category line or the end of file
            print("here", cat_index)
            if current_cat_index != None:
                lines[current_cat_index]=f"{lines[current_cat_index].rstrip("\n")} {round(cat_sub_total,2)}\n"
            cat_sub_total = 0
            current_cat_index = lines.index(line)
        elif (equals_index != -1):
            print(line[equals_index+1:])
            equals_sub = float(line[equals_index+1:].rstrip("\n"))
            cat_sub_total += equals_sub
            print(cat_sub_total)
            
    lines[current_cat_index]=f"{lines[current_cat_index].rstrip("\n")} {round(cat_sub_total,2)}\n"
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(lines)


sub_totals(path_to_file + file_name)

count_categories(path_to_file + file_name)


