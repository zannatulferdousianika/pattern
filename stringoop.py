class StringOperator:
    def __init__(self,text):
        self.text = text

    def to_upper(self):
        return self.text.upper()
    
    def to_lower(self):
        return self.text.lower()
    
    def reverse(self):
        self.text[::-1]

    def is_palindrome(self):
        self.text == self.text[::-1]

    def is_vowel(self):
        return sum(1 for char in self.text.lower() if char in 'aeiou')
    
    def replace_word(self,old,new):
        return self.text.replace(old,new)
    
    def find_word(self,word):
        return self.text.find(word)

    def word_count(self,text):
        return len(self.text.split())

    def remove_whitespace(self):
        return self.text.strip()

    def capitalized_word(self):
        return self.text.title()
    
if __name__ == "__main__":
    sentence = input("enter a sentence")
    operator = StringOperator(sentence)

    print("\nString methods:")
    print("Uppercase:", operator.to_upper())
    print("Lowercase:", operator.to_lower())
    print("Reverse:", operator.reverse())
    print("Palindrome:", operator.is_palindrome())
    print("Count vowels:", operator.is_vowel())
    print("Replace 's' with $ word:", operator.replace_word('s','$'))
    print("Find 'the' in sentence:", operator.find_word('the'))
    print("Word count:", operator.word_count())
    print("Space removed:", operator.remove_whitespace())
    print("Capitalized words:", operator.capitalized_word())


    








        
        
        
        
        
    

        
        
        
