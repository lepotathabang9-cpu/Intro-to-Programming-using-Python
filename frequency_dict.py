# Creating a Frequency dictionary that shows how many times a particular word appears in a song.

def frequency_dict(song:str):
    """
    frequency_dict: Accepts an iterable as input. Iterates through the iterable to count
    the number of times a specific words appears in a song. Each word and it's number of
    occurrences are added to a dictionary as key-value pairs.

    """
    word_dict = {}
    # Create a list containing the words of the song as the elements of the list
    words = song.lower().split()
    for word in words:
        if word in word_dict:
            # If the word is already in the dictionary, just increment it by 1
            word_dict[word] += 1
        else:
            # If the word is not inside the dictionary, then add the word and assign a value of 1
            word_dict[word] = 1
    return word_dict


# A function that returns the most frequent word
def most_freq(most:dict):
    """
    most_freq: Iterates through a dictionary and returns items with the highest values.
    most: dictionary passed as input.

    """
    words = []
    highest = max(most.values())
    for key, value in most.items():
        if value == highest:
            words.append(key)
    return (words, highest)

# Main is an Orchestrator function
def main():
    song = '''
    Never gonna give you up  
    Never gonna let you down  
    Never gonna run around and desert you  
    Never gonna make you cry  
    Never gonna say goodbye  
    Never gonna tell a lie and hurt you
    '''

    print(frequency_dict(song))
    print(most_freq(frequency_dict(song)))

if __name__ == "__main__":
    main() # If I run this python script directly, it will execute all the block of statements under main()

# Always keep in mind that in Python, functions must first be defined before they can be called.
