class Publication:
    def __init__(self, title: str, author: str):
        self.__title = title
        self.__author = author

   
    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author


    def set_title(self, title: str):
        self.__title = title

    def set_author(self, author: str):
        self.__author = author

    def display_info(self):
        print(f"Title: {self.__title}")
        print(f"Author: {self.__author}")


class Book(Publication):
    def __init__(self, title: str, author: str, number_pages: int):
        super().__init__(title, author)
        self.__number_of_pages = 1  # Default valid value
        self.set_number_of_pages(number_pages)


    def get_number_of_pages(self):
        return f"Number of pages: {self.__number_of_pages}"

    
    def set_number_of_pages(self, number_pages: int):
        if number_pages > 0:
            self.__number_of_pages = number_pages
        else:
            print("Number of pages must be positive.")


class Magazine(Publication):
    def __init__(self, title: str, author: str, issue_number: int):
        super().__init__(title, author)
        self.__issue_number = 1  # Default valid value
        self.set_issue_number(issue_number)


    def get_issue_number(self):
        return f"Issue number:{self.__issue_number}"

   
    def set_issue_number(self, issue_number: int):
        if issue_number > 0:
            self.__issue_number = issue_number
        else:
            print("The issue number must be positive.")


pub1 = Publication("Journal of Experimental Psychology", "Ratcliff, R. & Van Dongen, H.")
pub2 = Publication("Nature Communications", "Various Researchers")


book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("Noli Me Tangere", "Jose Rizal", 480)


mag1 = Magazine("National Geographic", "Various Authors", 202)
mag2 = Magazine("Time Magazine", "Time Editors", 150)



print("Publication Information:")
pub1.display_info()

print("\nPublication 2 Information:")
pub2.display_info()

print("\nBook Information:")
book1.set_number_of_pages(-310)  # Setting invalid value to test validation
book1.display_info()
print(book1.get_number_of_pages())

print("\nBook 2 Information:")
book2.display_info()
print(book2.get_number_of_pages())

print("\nMagazine Information:")
mag1.display_info()
print(mag1.get_issue_number())

print("\nMagazine 2 Information:")
mag2.set_issue_number(0)  # Testing zero validation on Magazine
mag2.display_info()
print(mag2.get_issue_number())
