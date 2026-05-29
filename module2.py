def invert_case_in_file(input_filename, output_filename):
    with open(input_filename, 'r', encoding='utf-8') as infile:
        text = infile.read()
    transformed_text = text.swapcase()
    with open(output_filename, 'w', encoding='utf-8') as outfile:
        outfile.write(transformed_text)
