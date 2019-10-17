from time import sleep
import datetime

NIGHT_STARTS = 19
DAY_STARTS = 8
HOUR_DURATION = 1


def write_file_and_screen(text, file_name):
    with open(file_name, "a") as hours_file:
        hours_file.write("{}{}".format(text, "\n"))
        print(text)


def main():
    current_time = datetime.datetime.now()
    is_nigth = False

    while True:
        sleep(HOUR_DURATION)
        current_time += datetime.timedelta(hours=1)
        light_changed = False

        if (current_time.hour > NIGHT_STARTS and current_time.hour <= DAY_STARTS) and not is_nigth:
            is_nigth = True
            light_changed = True

        elif(current_time.hour > DAY_STARTS and current_time.hour < NIGHT_STARTS) and is_nigth:
            is_nigth = False
            light_changed = True

        if light_changed:
            if is_nigth:
                write_file_and_screen("Se ha hecho de noche", "horas.txt")
            else:
                write_file_and_screen("Se ha hehco de dia","horas.txt")

        write_file_and_screen("La hora actual es {}".format(current_time), "horas.txt")


if __name__=="__main__":
    main()