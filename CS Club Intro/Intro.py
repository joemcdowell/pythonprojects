# This is a single-line comment
# useful for debugging or helpful notes

''' This is a multi-line comment
    Typing comments on multiple lines is helpful

    You can write a bunch of information without having to comment
        out every single line!

    It's self-explanatory but some people just don't understand it
        which is why their comments are annoying to read.
'''

''' to declare a function (in Java, a "Method")
        the 'def' keyword followed by the name of the function.
    Then parentheses, in which you may list the names of the function's
        arguments in their respective order, followed by a colon (':')

    for example:
        | def foo( bar, baz ):
        |     ...

    Note that you do not declare a return variable type, nor do you specify
        the types of any of the function's arguments. 

'''

''' This will serve as the 'main' method, although look at the bottom-most code
        for more information about this.
'''


def main():
    ''' unlike Java, there is no need for curly braces, which makes whiteboarding
            Python WAY easier
        Instead, the strict use of proper indentation serves in the place of
            curly braces
            -> Each level of indentation is 4 spaces. 2 spaces for indentation is wrong!
    '''

    variables()

    input("[Next] Operators")

    operators()

    input("[Next] Simple I/O")

    simple_io()

    input("[Next] Boolean Logic")

    boolean_logic()

    input("[Next] Looping")

    looping()

    input("[Next] File IO")

    file_io()

    input("[Next] Let's Apply some of this information")

    get_frequency()

    input("[Next]")

    classes()

    input("[END]")


def variables():
    ### VARIABLES ###

    number = 42  # An Integer value
    decimal_number = 12.34  # A floating point value
    name = "Adrian"  # A String
    ''' Strings:
            Strings in Python can be declared by using any quotation character

            "", '', """...""", etc.

            unlike in Java:
                these define a string, not a character -> ''

            Yes, multiple-line comments are essentially just unassigned strings
    '''
    boolean = True
    untrue = False

    test_scores = [84, 78, 82, 68, 97, 92, 89]  # An Array (closer to an Arraylist)

    a_tuple = ('John', 'Smith')  # a tuple is an array that may not be altered

    dictionary = {"age": 26, "name": "John", "isAlive": True}
    ''' a dictionary (similar to a Hashmap in Java) allows you to store data
            in a lookup-table. The data may be accessed by passing the 
            dictionary a reference value. (Like looking up a word's 
            definition in a dictionary, you look for the word!)
    '''
    print("John is {0} years old.".format(dictionary["age"]))


def operators():
    ### Operators ###

    print(1 == 1.0)  # True
    print(1 != 1.1)  # True
    print(1 > 1.1)  # False
    print(1.1 < 2)  # True
    print(1.5 >= 1.5)  # True
    print(1.5 <= 2)  # False

    # mathematical operators #
    x = 10

    ## Addition, Subtraction, Multiplication, Division
    x += 5  # x = x + 5
    x -= 3  # x = x - 3
    x *= 2  # x = x * 2
    x /= 4  # x = x / 4

    # Python also has exponents
    x **= 2  # x = x ** 2

    # Here's the modulus operator
    x %= 3  # x = x % 3


def simple_io():
    ### Simple I/O ###

    # Instead of that long, tedious: System.out.println("......");
    print("Hello, World!")

    # Instead of: Scanner keyboard = new Scanner(System.in); blah blah blah
    user_input = input("what's your name? >")

    print("Hello ", user_input)

    my_value = int(input("How old are you?"))
    print("Oh, you're {0}?".format(my_value))


def boolean_logic():
    ### Boolean Logic and program flow ###

    boolean, untrue = True, False

    ''' Keywords:

        Boolean values: True, False

        Comparators:    and, or, not

        If-Statement format:

            if (condition):
                ...
            elif (condition):
                ...
            elif (condition):
                ...
            ...
            else:
                ...
    '''

    if boolean and not untrue:  # (boolean && !untrue)
        print("This if-statement is true!")
    elif boolean:
        print("The first part is false, but second clause is true!")
    else:
        print("They're both false!")


def looping():
    ### Looping ###

    '''  Loops are nice and simple, no parentheses, semi-colons, etc

            while (condition):
                instructions

            for (iteratable):
                instructions

            Python for-loops are akin to Java for-each loops

            Iterables are things like lists
    '''

    x = 0  # counting variable

    while x < 10:
        x += 1
        print(x, end=' ')  # prints "1 2 3 4 5 6 7 8 9 10"

    for i in range(x):  # range(10) -> [0,1,2,3,4,5,6,7,8,9]
        print(i)

        if i % 2 == 0:  # check if i is even
            print("{0} is even".format(i))

        if i == 7:
            break  # exits the loop


def file_io():
    ### File I/O ###

    # Opening a file
    file = open("test.txt", 'r+')

    # Reading from a file
    line = file.readline()  # read a single line

    contents = file.read()  # read whole file

    print(contents)

    # Writing to a file
    file.write("This is the end of the file.")

    # Closing a file
    file.close()


def lists():
    # get some numbers from a file
    file = open("numbers", 'r')
    contents = file.read().strip()  # read contents

    # parse the values (strings into integers) into an array
    values = [int(x) for x in contents.split("\n")]

    # length of the list
    print("Length of list: ", len(values))

    # simple list output
    print(values)

    input('[I] Indexes')

    # lets set the values of the first 5 indexes to [0,1,2,3,4]
    for i in range(5):
        values[i] = i

    # Let's see what it looks like
    print(values)

    input('[II] Appending')

    # How about we add to the list! No need to redefine an array!
    values.append(20)

    print(values)

    input('[III] Slicing and Concatenation')

    # This outputs a list slice from indexes 0 to 5
    print("[0:5] -> ", values[0:5])

    # This is a list slice from index 0 to index 7
    print("[:7] -> ", values[:7])

    # This is a slice from index -2 (second to last index of list) to the end
    print("[-2:] -> ", values[-2:])

    # This shows list concatenation, which merges lists
    print("[-2:] + [:2]\n\t-> ", values[-2:] + values[:2])


def get_frequency():
    # get a string from the user
    statement = input("Statement > ")

    # This will contain our letter-frequencies
    # It is currently empty but will be filled
    frequencies = {}

    # iterate along the list, one character at a time
    for character in statement:

        # if we have not encountered the letter
        if character not in frequencies:
            # add an entry in the dictionary
            frequencies[character] = 0

        # increment the frequency of the letter
        frequencies[character] += 1

    # let's see what we have!
    print(frequencies)


class Rectangle:
    ''' The Rectangle class '''

    def __init__(self, height, width):
        self.height = height
        self.width = width

    def get_area(self):
        return (self.height * self.width)

    def __str__(self):
        return "[{0} by {1}]".format(self.height,
                                     self.width)


class Square(Rectangle):
    ''' Square class, child of Rectangle '''

    def __init__(self, side):
        self.height = side
        self.width = side


def classes():
    rect1 = Rectangle(3, 4)

    print(rect1)
    print("rect1's area is :", rect1.get_area())

    input("[I] Square?")

    sqr1 = Square(3)
    print(sqr1)
    print("sqr1's area is :", rect1.get_area())


if __name__ == '__main__':
    main()