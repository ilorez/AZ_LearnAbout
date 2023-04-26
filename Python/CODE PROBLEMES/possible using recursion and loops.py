def generate_permutations(string, step = 0):

	# if we've gotten to the end, print the permutation
    if step == len(string):
        print("".join(string))

	# everything to the right of step has not been swapped yet
    for i in range(step, len(string)):

		# copy the string (store as array)
        string_copy = [character for character in string]

		# swap the current index with the step
        string_copy[step], string_copy[i] = string_copy[i], string_copy[step]

		# recurse on the portion of the string that has not been swapped yet (now it's index will begin with step + 1)
        generate_permutations(string_copy, step + 1)

# example
string = "ABCD"
generate_permutations(string)

"""def generate_permutations(string):

    # get the length of the string
    n = len(string)

    # a list to store all permutations
    permutations = []

    # loop through all possible indices
    for i in range(n):

        # get the character at the index
        char = string[i]

        # create a temporary string
        temp_string = string

        # remove the character from the string
        temp_string = temp_string.replace(char, "")

        # loop through the rest of the characters
        for j in range(len(temp_string)):

            # add the character to the beginning of the string
            new_string = temp_string[j] + temp_string[:j] + char

            # append the new string to the list of permutations
            permutations.append(new_string)

    # return the list ofcpermutations
    return permutations

# example
string = "ABC"
print(generate_permutations(string))"""