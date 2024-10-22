def morning_message(date, fname, percent, temp):
    nice_msg = ""
    if temp < 70:
        nice_msg = "Have a chilly day!"
    elif 71 <= temp <= 80:
        nice_msg = "Have a beautiful day!"
    elif temp > 80:
        nice_msg = "Have a scorching day!"
    
    print(f"Good Morning {fname}, today is {date}. The temperature is {temp}F. There is a {percent*100}% chance of rain. {nice_msg}")
    
morning_message( "10/21/2024", "Christy", 0.6, 67)

morning_message( "10/21/2024", "Misty", 0.2, 81)

morning_message( "10/21/2024", "Bob", 0.8, 99)
    
