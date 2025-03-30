
#opening the file and creating dictionary
with open('nato_phonetic_alphabet.csv') as f:
    nato_alphabet = f.readlines()
    nato_alphabet = [item.strip('\n') for item in nato_alphabet]
    nato_alphabet = [item.split(',') for item in nato_alphabet]
    nato_alphabet.pop(0)
    nato_dict = {item[0]:item[1] for item in nato_alphabet}

def generate():
    #name input that converts name into uppercase and slices it into list
    name = [*input("Enter name: ").upper()]

    #creating list with items that corresponds to name letters
    try:
        name_letters = [nato_dict[letter] for letter in name]
    except:
        print("Only letters of the alphabet.")
        generate()
    else:
        #printing the result
        print(name_letters)

generate()