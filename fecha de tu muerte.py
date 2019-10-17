
import datetime

AVEANGE_LIFESPAN = 80

SMOKER_PENALIZAZION = 10
DRINKER_PENALIZACION = 10
SEDENTARY_PENALIZACION = 20


def print_with_underscores(message):
    print(message)
    print(len(message) * "-")


def ask_yes_or_not(message):
    response = None
    while response != "S" and response != "N":
        response = input(message + "  [S/N]")
    return response == "S"


print_with_underscores("Averigua cuanto te queda de vida")
print_with_underscores("Completa esta encuesta para saberlo")

birth_date = input("Cual es tu fecha de nacimiento ? (formato:dd/mm/yyyy) ?")

birth_date = datetime.datetime.strptime(birth_date, "%d/%m/%Y")
years_lost = 0


if ask_yes_or_not("Fumas?"):
    years_lost += SMOKER_PENALIZAZION
if ask_yes_or_not("Bebes?"):
    years_lost += DRINKER_PENALIZACION
if ask_yes_or_not("Haces deporte?"):
    years_lost += SEDENTARY_PENALIZACION


lifespan = AVEANGE_LIFESPAN - years_lost
death_day = birth_date + datetime.timedelta(days=lifespan*365)
days_to_death = death_day - datetime.datetime.now()

print("Fecha de muerte {}, te quedan {} dias para morir".format(death_day.strftime("%d/%m/%Y"), days_to_death.days))
