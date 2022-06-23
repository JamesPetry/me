"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement.

TODO: Start a list of important programming vocabulary in your readme.md for 
this week. E.g. the word "calling" means something in a programming context, 
what does it mean?
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

some_words = ["what", "does", "this", "line", "do", "?"]

# I think this will repeat the some_words string and with the print cmd it will print it in the terminal 
for word in some_words:
    print(word)
# It printed the statement

# I think it will print the some_words statement because the statement has been defined as x and it has a print cmd
for x in some_words:
    print(x)
# It printed x as the some_words string again

#this will print the some_words string
print(some_words)
#it printed the string in its written code form

#it will print whether the some_words string has more than 3 individual words in it
if len(some_words) > 3:
    print("some_words contains more than 3 words")
#it stated that the some_words string had more than three words in it


def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
# I think it will give information about the os, system info and software info
    print(platform.uname())
# it states the name of the device, system type, release of system and version aswell as the type of machine

usefulFunction()
