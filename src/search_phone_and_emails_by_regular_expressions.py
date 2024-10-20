import re


def find_phone_numbers(text: str):

    phone_pattern = re.compile(r'(?:[1-9]\d{9}|\d{3}-\d{2}-\d{2}|(?:\+7|7|8)\s*[-]?\(?\d{3}\)?[\s-]?\d{3}[\s-]?\d{2}[\s-]?\d{2})', re.MULTILINE)
    phones = phone_pattern.findall(text)

    email_pattern = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')
    emails = email_pattern.findall(text)

    return phones, emails


filename = '../text/mail.txt'

with open(filename, 'r', encoding='utf-8') as file:
    mail_text = file.read()

result_phones, result_emails = find_phone_numbers(text=mail_text)

print("Найденные номера:\n", "\n".join(result_phones))
print("\nНайденные email:\n", "\n".join(result_emails))
