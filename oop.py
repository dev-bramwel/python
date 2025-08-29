# Assignment 1: Design Your Own Class! 🏗️
# Example: Book class with inheritance

class Book:
	def __init__(self, title, author, pages):
		self.title = title
		self.author = author
		self.pages = pages
		self.is_open = False
    
	def open_book(self):
		self.is_open = True
		print(f"Opening '{self.title}' by {self.author}.")
    
	def close_book(self):
		self.is_open = False
		print(f"Closing '{self.title}'.")

# Inheritance: EBook is a type of Book
class EBook(Book):
	def __init__(self, title, author, pages, file_size):
		super().__init__(title, author, pages)
		self.file_size = file_size  # in MB
    
	def download(self):
		print(f"Downloading '{self.title}' ({self.file_size}MB)...")

# Demonstrate encapsulation (private attribute)
class SecretBook(Book):
	def __init__(self, title, author, pages, secret_code):
		super().__init__(title, author, pages)
		self.__secret_code = secret_code  # private attribute
	def reveal_secret(self):
		print(f"Secret code for '{self.title}': {self.__secret_code}")

# Activity 2: Polymorphism Challenge! 🎭
class Vehicle:
	def move(self):
		print("Vehicle is moving...")

class Car(Vehicle):
	def move(self):
		print("Driving 🚗")

class Plane(Vehicle):
	def move(self):
		print("Flying ✈️")

class Boat(Vehicle):
	def move(self):
		print("Sailing 🚤")

if __name__ == "__main__":
	# Assignment 1 demo
	book1 = Book("1984", "George Orwell", 328)
	ebook1 = EBook("Digital Fortress", "Dan Brown", 356, 2.5)
	secret_book = SecretBook("Secret Files", "Agent X", 100, "XYZ123")
	book1.open_book()
	ebook1.download()
	secret_book.reveal_secret()
	book1.close_book()

	print("\nPolymorphism Challenge:")
	vehicles = [Car(), Plane(), Boat()]
	for v in vehicles:
		v.move()
