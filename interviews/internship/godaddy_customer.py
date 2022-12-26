class LibraryManagementSystem:
    "This is a libraryManagementSystem class"
    userType = ""
    username = ""
    password = ""

    def login(self):
        print('Hello, you are logged in')

    def register(self):
        print('You are registered')

    def logout(self):
        print('You are logged out.')

class Book:
    title = ""
    author = ""
    isbn = ""
    publication = ""

    def bookinfo(self):
        print("Title: {}, Author: {}, ISBN: {}, Publication: {}".format(self.title, self.author, self.isbn, self.publication))
    



# Output: <function LibraryManagementSystem.userType>
print(LibraryManagementSystem.userType)

# Output: <function LibraryManagementSystem.username>
print(LibraryManagementSystem.username)

# Output: "This is a LibraryManagementSystem class"
print(LibraryManagementSystem.__doc__)

bookOne = Book()
bookOne.title = "Dictionary"
bookOne.bookinfo()