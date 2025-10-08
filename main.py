"""
# TODO: Write a program that determines the grade based on a score
# (A: 90-100, B: 80-89, C: 70-79, D: 60-69, F: below 60)
score = float(input("Entre une note entre 0 et 100 : "))

if score < 60:
    print("F ... tié rincé")

elif score < 70:
    print("ah faut bosser chef, D ..")

elif score < 80:
    print("c'est ok mais tu peux faire mieux, t'as eu C")    

elif score < 90:
    print("pas mal t'as eu B !")

elif score <= 100:
    print("ggwp t'as eu un A !")

else:
    print("Entre 0 et 100 on t'a dit")
"""
 
# TODO: Create a simple calculator that performs different operations
# based on user input (addition, subtraction, multiplication, division)
"""
nb1 = float(input("Entrez un 1er nombre : "))
nb2 = float(input("Entrez un 2e nombre : "))
operator = input("Choisissez une opération entre +, -, *, / : ")     

if operator != "+" and operator != "-" and operator != "*" and operator != "/":
    print("Mets un bon opérateur")

elif operator == "+":
    print(f"{nb1} + {nb2} = {nb1+nb2}")

elif operator == "-":
    print(f"{nb1} - {nb2} = {nb1-nb2}")

elif operator == "*":        
    print(f"{nb1} x {nb2} = {nb1*nb2}")

elif operator == "/":
    if nb2 != 0:
        print(f"{nb1} / {nb2} = {nb1/nb2}")
    else:
        print(f"La division par {nb2} est impossible")
"""
"""
# TODO: Write a program that checks if a year is a leap year
year = int(input("Entrez une année : "))

if year % 4 == 0:
    print(f"L'année {year} est bissextile")

else:
    print(f"L'année {year} n'est pas bissextile")
"""

# TODO: Implement a program that determines the price of a movie ticket
# based on age (child, adult, senior) and day of the week

movie_ticket = {
    "age": 18,
    "day": "Monday",
    "price": 10
}

movie_ticket["age"] = int(input("Entrez votre age : "))

if movie_ticket["age"] < 18:
    movie_ticket["price"] = 6.50
    print(f"Voici le tarif pour les mineurs : {movie_ticket['price']} €")

elif movie_ticket["age"] < 60:
    movie_ticket["price"] = 10
    print(f"Voici le tarif pour les adultes : {movie_ticket['price']} €")

elif movie_ticket["age"] >= 60:
    movie_ticket["price"] = 8.50
    print(f"Voici le tarif pour les séniors : {movie_ticket['price']} €")

else:
    print("Donnez un age valide")