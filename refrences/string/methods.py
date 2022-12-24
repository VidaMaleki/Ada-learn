#use a dictionary with ascii codes to replace 83 (S) with 80 (P):
mydict = {83:  80}

txt = "Hello Sam!"

print(txt.translate(mydict))
#Hello Pam!
#https://www.w3schools.com/charsets/ref_html_ascii.asp#:~:text=ASCII%20is%20a%207%2Dbit,are%20all%20based%20on%20ASCII.
