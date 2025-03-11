def find_the_redheads(family_dict):
    # Use the filter function to get names of individuals with red hair
    redheads = list(filter(lambda name: family_dict[name] == 'red', family_dict))
    return redheads

# Example usage
if __name__ == "__main__":
    dupont_family = {
        "florian": "red",
        "marie": "blond",
        "virginie": "brunette",
        "david": "red",
        "franck": "red"
    }
    
    # Print the result of the find_the_redheads method
    print(find_the_redheads(dupont_family))
    