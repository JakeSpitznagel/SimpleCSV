def parse(csv_input, file=False):
    """
        parse a comma separated string or file to print and return a list containing key/value pairs such that the value
        is the max value for each key in the initial string or file.

        behaviour only defined for input of the form: newline separated key/value pairs
            -eg. '1,2\n2,3\n3,4'
    :param csv_input: string: comma separated string or file name.
    :param file: bool: indicating the given string is a file
    :return: sorted list of unique key/value pairs containing the max value of each key in the CSV
    """
    if file:
        with open(file, 'r') as f:
            csv_input = f.read()
    list1 = [line.split(',') for line in csv_input.splitlines()]
    keys = {key for key, val in list1}
    final = []

    for key in keys:
        temp = [(x, int(y)) for x, y in list1 if x == key]
        final.append(max(temp))

    final.sort()
    print(final)
    return final

def parse_file(file):
    with open(file, 'r') as f:
        parse(f.read())


s = '1,2\n2,3\n3,4'

if __name__ == "__main__":
        parse(s)
