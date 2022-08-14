input_str = "AI4Climate"
# Printing original string
print("Original string: " + input_str)
result_str = ""
for i in range(0, len(input_str)):
    if i != 2:
        result_str = result_str + input_str[i]
    # Printing string after removal
print("String after removal of i'th character : " + result_str)