# Takes a URL from the clipboard, sanitizes it, and writes it back to the clipboard
# Good for sending to clients, posting in tickets, etc
# J. Walsh 11.15.2022

import pyperclip
malUrl = pyperclip.paste()

# print("Input suspicious URL:")
# malUrl = input("> ")

str = malUrl
cattivo = (str.replace("http", "hxxp"))

str = cattivo
safeUrl = (str.replace(".", "[.]"))
print(safeUrl)

print("Sending to clipboard")


pyperclip.copy(safeUrl)

pause(30)

print("done")

close = input("> ")
