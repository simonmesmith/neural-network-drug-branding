import string

# Get text and lowercase it. (Assumption: Lowercase to reduce the number of unique characters.)
def getText(inputFilename):
    return open('inputs/' + inputFilename).read().lower()

# Get unique characters from the text in list format in ascending order.
def getChars(text):
    return sorted(list(set(text)))

# Create a character index array for the unique characters (e.g. ['a': 0, 'b': 1]).
def getCharIndices(chars):
    return dict((c, i) for i, c in enumerate(chars))

# Create another character index array that's the inverse of char_indices (e.g. ['0': a, '1': b]).
def getIndicesChar(chars):
    return dict((i, c) for i, c in enumerate(chars))

def cleanOutput(outputFilename, minOutputLength=3):
    cleaned = []
    with open('outputs/' + outputFilename) as f:
        for line in f:
            if (len(line.strip()) > minOutputLength):
                cleaned.append(line)
    outputFile = open('outputs/' + outputFilename, "w")
    outputFile.write(''.join(cleaned)) # Adding with '\n' added additional line break; not sure why, but to do: figure this out and join with line breaks in a way that creates only one new line per output row
    outputFile.close()
