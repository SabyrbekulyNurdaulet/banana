# 6. Напишите метод, заменяющий в строке все вхождения слова «бяка» на «вырезано цензурой».

def censor_word(text, target_word, replacement):
    return text.replace(target_word, replacement)

# Пример использования метода
text = input("Введите строку: ")
censored_text = censor_word(text, "бяка", "вырезано цензурой")

print(censored_text)  # "Эта вырезано цензурой совсем надоела, как и другая вырезано цензурой."
