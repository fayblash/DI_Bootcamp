import json
import nltk
from nltk.corpus import stopwords
nltk.download('punkt')
nltk.download('stopwords')
from nltk.tokenize import word_tokenize
# Instructions :
# Download my_text.txt

# Create a class called Text that takes a string as an argument and store the text in a attribute.
class Text():
    def __init__(self,string):
        self.string=string
# Implement the following methods:
# a method to return the frequency of a word in the text (assume words are separated by whitespace) return None or a meaningful message .
    def frequency(self,word):
        pass
# a method that returns the most common word in the text.
    def common(self):
        temp_list=self.string.split(" ")
        from collections import Counter
        word_counts = Counter(temp_list)
        most_common = word_counts.most_common(1)
        return most_common
# a method that returns a list of all the unique words in the text.
    def unique(self):
        unique_list = set(self.string.lower().split(" "))
        return unique_list
# a classmethod that returns a Text instance but with a text file: >>> Text.from_file('my_text.txt')
    # @classmethod
    
# Create a class called TextModification that inherits from Text.
class TextModification(Text):
    def __init__(self,string):
        super().__init__(string)    
# Implement the following methods:
# a method that returns the text without any punctuation.
    # def no_punc(self):
    #     return re.sub('[^A-Za-z ]+', '', self.string)    
# a method that returns the text without any english stop-words (check out what this is !!).
    # def no_stopwords(self):
    #     text_tokens = word_tokenize(self.string)
    #     tokens_without_sw = [word for word in text_tokens if not word in stopwords.words()]
    #     return tokens_without_sw
# a method that returns the text without any special characters.

# Now, use the provided txt file and try using the class you created above.
# Note: Note: Feel free to implement/create any attribute, method or function needed to make this work, be creative :)

f = open('the_stranger.txt')
textstring = f.read()
f.close()

new_text=TextModification(textstring)

print(new_text.common())
# print(new_text.unique())
# print(new_text.no_punc())
print(new_text.string)
# print(new_text.no_stopwords())
