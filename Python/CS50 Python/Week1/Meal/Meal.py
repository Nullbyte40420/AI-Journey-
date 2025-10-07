def main():
    time_str=input("What time is it? ")
    time=convert(time_str)

    if 7<= time <=8:
        print("breakfast time")
    elif 12<= time <=13:
        print("lunch time")
    elif 18<= time<=19:
        print("dinner time")

def convert(time):
    time=time.strip().lower()
    if "pm" in time or "am" in time:
        parts=time.replace("pm", "").replace("am", "").strip().split(":")
        hours=int(parts[0])
        minutes=int(parts[1])

        if "pm" in time and hours!=12:
            hours += 12
        if "am" in time and hours==12:
            hours =0
        return int(hours) + int(minutes)/60
    else:
        hours,minutes=time.split(":")
        return int(hours) + int(minutes)/60

if __name__ == "__main__":
    main()

