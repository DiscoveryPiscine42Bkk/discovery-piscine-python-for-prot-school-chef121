def array_of_names(names_dict):
    # Initialize an empty list to store the full names
    full_names = []
    
    # Iterate over the dictionary and format the names
    for first_name, last_name in names_dict.items():
        # Capitalize first letters and combine the names
        full_name = f"{first_name.capitalize()} {last_name.capitalize()}"
        full_names.append(full_name)
    
    return full_names

# Example usage
if __name__ == "__main__":
    persons = {
        "jean": "valjean",
        "grace": "hopper",
        "xavier": "niel",
        "fifi": "brindacier"
    }
    
    # Print the result of the method
    print(array_of_names(persons))