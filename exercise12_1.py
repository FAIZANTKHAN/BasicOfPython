with open("stock.csv", "r") as f, open("output.csv", "w") as out:
    out.write("Company Name,PE Ratio, PB Ratio\n")
    next(f)  # This will skip the first line in the file, assuming it's a header
    for line in f:
        tokens = line.strip().split(",")  # Remove leading/trailing whitespaces and split by comma
        if len(tokens) >= 4:  # Ensure at least 4 columns exist
            stock = tokens[0]
            try:
                price = float(tokens[1])
                eps = float(tokens[2])
                book = float(tokens[3])
                pe = round(price / eps, 2)
                pb = round(price / book, 2)
                out.write(f"{stock},{pe},{pb}\n")
            except (IndexError, ValueError):
                print(f"Error processing line: {line}")
                continue
        else:
            print(f"Issue with line: {line}")
