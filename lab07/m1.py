with open("text.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

total_lines = len(lines)
total_words = 0
total_chars = 0

longest_line_num = 0
longest_line_len = -1
longest_line_text = ""

for index, line in enumerate(lines, start=1):
    clean_line = line.rstrip("\r\n")
    total_words += len(clean_line.split())
    total_chars += len(clean_line)
    
    if len(clean_line) > longest_line_len:
        longest_line_len = len(clean_line)
        longest_line_num = index
        longest_line_text = clean_line

print(f"Рядків: {total_lines}")
print(f"Слів: {total_words}")
print(f"Символів: {total_chars}")
if total_lines > 0:
    print(f"Найдовший рядок: №{longest_line_num}, {longest_line_len} символів")
    print(f"Текст: {longest_line_text}")
