class TextAnalyzer():
    def __init__(self, text):
        self.text = text
        if text == "":
             raise Exception("Text cannot be empty")

        self.text = text

    def __str__(self):
        words = self.text.split()
        return f"TextAnalyzer object with {len(words)} words"

    def __len__(self):
        return len(self.text)

    def word_count(self):
        return len(self.text.split())

    def count_word(self, word):
        if word == "":
            raise Exception("Word cannot be empty")

        words = self.text.split()
        return words.count(word)
