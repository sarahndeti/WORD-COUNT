__author__ = 'Sarah'

def words(text):
    """

    :rtype :
    """
    split_list =  text.split()
    split_list = [int(x) if x.isdigit() else x for x in split_list]
    word_count = {}

    while True:

        length = len(split_list)
        element = split_list[0]

        number = 0
        if (length <= 0):
            return word_count
        elif(length == 1):
            number = 1
            word_count[element] = 1
            return word_count

        for i in range(0, len(split_list)):
            if split_list[i] == element:
                number+=1

        word_count[element] = number
        split_list[:] = (value for value in split_list if value !=element)
        number = 0
        element = ""

print words("one fish two fish red fish blue fish")
print words("testing 1 2 testing")
