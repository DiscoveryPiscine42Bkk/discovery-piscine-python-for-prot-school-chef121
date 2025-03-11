def famous_births(people_dict):
    # Sort the dictionary by the date of birth (as integers for correct sorting)
    sorted_people = sorted(people_dict.values(), key=lambda x: int(x['date_of_birth']))
    
    # Display the sorted information
    for person in sorted_people:
        print(f"{person['name']} is a great scientist born in {person['date_of_birth']}.")

# Example usage
if __name__ == "__main__":
    women_scientists = {
        "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
        "cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
        "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
        "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
    }
    
    # Call the method to display sorted results
    famous_births(women_scientists)