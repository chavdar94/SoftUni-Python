from string import punctuation

with open('text.txt', 'r') as input_file:
    with open('output.txt', 'w') as output_file:
        for line, data in enumerate(input_file, 1):
            ch_count = sum([1 for x in data if x.isalpha()])
            punct = sum([data.count(symbol) for symbol in punctuation])
            # for ch in data:
            #     if ch.isalpha():
            #         ch_count += 1
            #     elif ch in punctuation:
            #         punct += 1
            output_file.write(f"Line {line}: {data.strip()} ({ch_count})({punct})\n")
