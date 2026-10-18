from text_analyzer import TextAnalyzer

text = "Python is fun and Python is powerful"

analyzer = TextAnalyzer(text)

print(analyzer)
print(len(analyzer))
print(analyzer.word_count())
print(analyzer.count_word("Python"))


# Test 1: Empty text
try:
    analyzer = TextAnalyzer("")
except Exception as e:
    print(e)

# Test 2: Empty word
try:
    analyzer.count_word("")
except Exception as e:
    print(e)
