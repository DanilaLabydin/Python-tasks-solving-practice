# Write simple .camelCase method (camel_case function in PHP, CamelCase in C# or camelCase in Java) for strings.
# All words must have their first letter capitalized without spaces.


def camel_case(string):
    # your code here
    return string.title().replace(" ", "")


print(camel_case("hello case"))
