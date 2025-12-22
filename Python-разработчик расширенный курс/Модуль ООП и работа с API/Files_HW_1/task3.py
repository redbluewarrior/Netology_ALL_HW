

def string_count(string):
    with open(string, 'r', encoding='utf-8') as text:
        lines = len(text.readlines())
        return lines

def text_read(text):
    with open(text, 'r', encoding='utf-8') as reader:
        text = reader.read()
        return text

def text_write(text):
    with open('Result.txt', 'w', encoding='utf-8') as writer:
        result_txt = writer.write(text)
        return result_txt

texts = ['1.txt', '2.txt', '3.txt']

lines = {}
result = ""
for text in texts:
    lines[text] = string_count(text)


sorted_lines = sorted(lines.items(), key=lambda item: item[1])


for text, lines in sorted_lines:
    result += f'{text}\n{lines}\n{text_read(text)}\n'

text_write(result)

print(result)









