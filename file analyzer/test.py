from analyzer import FileAnalyzer

analyzer = FileAnalyzer()

file = input("Input your File: ")

analyzer.read_file(file)

print(f'File: {file}')
print(f'Words: {analyzer.word_count(file)}')
print(f'Lines: {analyzer.line_count(file)}')
print(f'Characters: {analyzer.char_count(file)}')
print(f'Top Three Words: {analyzer.word_freq(file)}')