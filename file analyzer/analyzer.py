import os
class FileAnalyzer():
    # Set the full path
    def full_path(self, file_name):
        # The folder this script is in
        script_dir = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(script_dir, file_name)

    
    ### Read the file
    def read_file(self, file_name):
        full_path = self.full_path(file_name)

        with open(full_path, 'r') as file:
            return file.read()
    

    # Count the words in the file
    def word_count(self, file_name):
        # Gets the word count of this file
        content = self.read_file(file_name)
        return len(content.split())
    
    # Count the lines in the file
    def line_count(self, file_name):
        content = self.read_file(file_name)
        return len(content.splitlines())
    

    # Count amount of characters
    def char_count(self, file_name):
        content = self.read_file(file_name)
        return len(content)
    

    # Word Frequency using lists
    def word_freq(self, file_name):
        word_count = dict()

        # Read the file. Make all words lower case and remove all punctuation and whitespace.
        content = self.read_file(file_name).lower().replace(',', '').replace('.', '').split()

        # Loop through each word in content and check if the word is already in the empty word_count dictionary
        # If word is in the dict then add 1 to its key value. If not, add the word to the dictionary
        for word in content:
            if word in word_count:
                word_count[word] = word_count[word] + 1
            else:
                word_count[word] = 1
        
        # Get the top 3 items using a lambda function and sorted()
        sorted_words = sorted(word_count.items(), key = lambda item: item[1], reverse=True)
        return sorted_words[:3]
            
        
        
    
