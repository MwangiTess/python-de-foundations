# Step 1: Open the file in Python

with open('sales.csv', 'r') as file:
    print("File opened successfully")

# Step 2: Read the first line(header row)
    header_line = file.readline().strip()
    print(header_line)

# Step 3: Split the header into column names.

    columns = header_line.split(",")
    print(columns)

# Step 4: Read the remaining lines(the data)
    for line in file:
        clean_line = line.strip()
        # Step 5: Split each row into fields
        fields = clean_line.split(",")
        # print(clean_line)
        # print(fields)

        # Step 6: Pair each field with its column name
        for i in range(len(fields)):
            col_name = columns[i]
            value = fields[i].strip()
            # Step 7: Clean each field and detect its type
            if value == "":
                detected = "MISSING"
            elif value.isdigit():
                detected = "int"
            elif value.count(".") == 1 and value.replace(".", "").isdigit():
                detected = "float"
            else:
                detected = "str"
            print(col_name, "→", repr(value), "|", detected)
            # repr(value) prints the value wih its quotes visible
            # Step 8 — Add a data quality flag
            if col_name == "amount" and detected not in ("float", "int"):
                print("⚠ WARNING: amount should be numeric got:", repr(value))
        print("---")  # puts a separator btwn rows so the output is readable.
