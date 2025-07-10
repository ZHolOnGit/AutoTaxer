import camelot
from tabulate import tabulate

# file_arr = ["Sept.pdf","Nov.pdf","Oct.pdf"]
file_arr = ["Sept.pdf"]

for file in file_arr:
    path = "data/" + file
    tables = camelot.read_pdf(path, flavor="stream", pages="all", table_areas=["50,520,550,70"])
    camelot.plot(tables[0], kind="contour").show()
    for i in range(tables.n):
        print(i)
        table = tables[i].df
        print(tabulate(table, headers = 'keys', tablefmt = 'psql'))


def clean_table(df, check_row):
    merged_rows = []

    for _, row in df.iterrows():
        if row[check_row] == '':
            merged_rows.append(row)
            