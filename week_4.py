# File Read & Write Challenge 🖋️ and Error Handling Lab 🧪
def main():
	filename = input("Enter the filename to read: ")
	try:
		with open(filename, 'r') as infile:
			content = infile.read()
			print("File read successfully!")
	except FileNotFoundError:
		print(f"Error: The file '{filename}' does not exist.")
		return
	except IOError:
		print(f"Error: The file '{filename}' could not be read.")
		return

	# Modify the content (for example, convert to uppercase)
	modified_content = content.upper()

	# Write the modified content to a new file
	new_filename = f"modified_{filename}"
	try:
		with open(new_filename, 'w') as outfile:
			outfile.write(modified_content)
		print(f"Modified content written to '{new_filename}'")
	except IOError:
		print(f"Error: Could not write to '{new_filename}'.")

if __name__ == "__main__":
	main()
