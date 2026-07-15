import re

path_to_file = "/Users/zaza/Main/ObsidianVault/Brain/"

file_name = "Maytest.md"

TOTAL_IN=2100
NUMBER_REGEX=r"[-+]?\d*\.?\d+"

def sub_totals(file_path):

    with open (file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    modified_lines = []
    for line in lines:
        dash_index = line.find("-")
        numbers = [float(x) for x in re.findall(NUMBER_REGEX, line)]
        if len(numbers) != 0:
            total = sum(numbers)
            new_line = f"{line.rstrip("\n")} = {total:.2f}\n"
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

def out_report_generator(file_path):
    total_out = []
    with open (file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    sub_report = []
    for line in lines:
        cat_index = line.find("##")
        if cat_index != -1:
            cat_total = re.search(NUMBER_REGEX, line).group()
            total_out.append(float(cat_total))
            sub_report.append(f"- {line[2:]}")
    
    rounded_total = round(sum(total_out),2)

    output = [
    f"# Total in - {TOTAL_IN} \n"
    f"# Total out - {rounded_total} \n"
    f"# Profit - {round(TOTAL_IN - rounded_total,2)} \n"
    f"## Out report - {rounded_total} \n"
    ]

    for sub in sub_report:
        output.append(f"{sub}")
    
    updated_file = lines[:3] + output + lines[3:]
    print(output)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(updated_file)


def main():
    sub_totals(path_to_file + file_name)

    count_categories(path_to_file + file_name)

    out_report_generator(path_to_file + file_name)


main()









