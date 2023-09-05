#referinte python regex https://www.w3schools.com/python/python_regex.asp
#docs oficial https://docs.python.org/3/library/re.html
import re #libraria regex, regular expressions

text = """Emailul meu este nume.prenume@gmail.com si numarul meu de telefon este 075841. 
Emailul colegei mele este nume2.prenume2@gmail.com si telefonul este 054879"""

email_pattern = r"\b\w+\.\w+@gmail\.com\b"

emailuri = re.findall(email_pattern, text)
print(emailuri)

tel_pattern = r"\b0\d{5}"
telefoane = re.findall(tel_pattern, text) # findall returneaza o lista cu elementele gasite
print(telefoane)

email_exista_in_text = re.search(email_pattern, text) #search gaseste primul element care satisface pattern
print(email_exista_in_text)

if email_exista_in_text:
    print("A gasit cel putin un email")
else:
    print("Nu a gasit nici un email in text")

#re.sub -face substituirea elementelor dupa pattern
text_nou =  re.sub(tel_pattern, "----", text)
print(text_nou)
#in cazul acesta a substituit toate numerele de telefon cu ----

#re.split- desparte textul in mai multe sub-texte dupa un pattern
clienti = re.split(tel_pattern, text)
print(clienti)




