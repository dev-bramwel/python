# Add timer functionality
import threading
import sys

def timeout():
	print("\nTime is up! Program will exit.")
	sys.exit(1)

# Function to calculate the final price after applying discount
def calculate_discount(price, discount_percent):
	"""
	Returns the final price after applying discount if discount_percent >= 20.
	Otherwise, returns the original price.
	"""
	if discount_percent >= 20:
		discount_amount = price * (discount_percent / 100)
		return price - discount_amount
	else:
		return price

if __name__ == "__main__":
	

	try:
		# Prompt user for input
		price = float(input("Enter the original price of the item: "))
		discount_percent = float(input("Enter the discount percentage: "))
		final_price = calculate_discount(price, discount_percent)
		if discount_percent >= 20:
			print(f"Final price after {discount_percent}% discount: {final_price}")
		else:
			print(f"No discount applied. Final price: {final_price}")
	except ValueError:
		print("Please enter valid numbers for price and discount percentage.")

