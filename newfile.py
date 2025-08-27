# Step 1: Read contents of input.txt
with open("input.txt", "r") as file:
    content = file.read()

# Step 2: Count words
word_count = len(content.split())

# Step 3: Convert text to uppercase
uppercase_content = content.upper()

# Step 4: Write processed text and word count to output.txt
with open("output.txt", "w") as file:
    file.write(uppercase_content)
    file.write(f"\n\nWord Count: {word_count}")

# Step 5: Print success message
print("Processing complete! 'output.txt' created successfully.")
