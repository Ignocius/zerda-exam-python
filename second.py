# Create a function that takes a filename and a string as parameter,
# And writes the string got as second parameter into the file 10 times.
# If the writing succeeds, the function should return True.
# If any problem raises with the file output, the function should not break, but return False.
# Example: when called with the following two parameters: "tree.txt", "apple",
# the function should write "appleappleapple" to the file "tree.txt", and return True.

def file_writer_ten_times_in_one_run(file_name, string_input):
    try:
        f = open(file_name, "w")
        for file_writer_runner in range(10):
            f.write(string_input)
        return True
    except IOError:
        return False

print(file_writer_ten_times_in_one_run("tree.txt", "apple"))
print(file_writer_ten_times_in_one_run("", "apple"))
