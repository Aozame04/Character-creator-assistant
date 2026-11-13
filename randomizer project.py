# The randomizer code
import random
from tkinter import *

prompt_file = "prompts.txt" # reads the file
with open(prompt_file) as file:
    lines = file.read().splitlines() #reads lines and splits them
    genderlist = [string.strip() for string in lines[0].removeprefix("Gender: ").split(',')] # reads as string and removes prefix and splits them into separate words
    staturelist = [string.strip() for string in lines[1].removeprefix("Stature: ").split(',')]
    agelist = [string.strip() for string in lines[2].removeprefix("Age: ").split(',')]
    specieslist = [string.strip() for string in lines[3].removeprefix("Species: ").split(',')]
    joblist = [string.strip() for string in lines[4].removeprefix("Job or title: ").split(',')]
    mainlist = [string.strip() for string in lines[5].removeprefix("Main characteristic: ").split(',')]
    featurelist = [string.strip() for string in lines[6].removeprefix("Features: ").split(',')]
    itemlist = [string.strip() for string in lines[7].removeprefix("Item: ").split(',')]
    superslist = [string.strip() for string in lines[8].removeprefix("Super natural ability: ").split(',')]
    animallist = [string.strip() for string in lines[9].removeprefix("Animal aspect: ").split(',')]
    environmentlist = [string.strip() for string in lines[10].removeprefix("Environment: ").split(',')]
    settinglist = [string.strip() for string in lines[11].removeprefix("Setting: ").split(',')]

def randomize():
    global stature, age, gender, species, job, main, feature, item, supers, animal, environment, setting
    reroll_gender()
    reroll_stature()
    reroll_age()
    reroll_species()
    reroll_job()
    reroll_main()
    reroll_feature()
    reroll_item()
    reroll_supers()
    reroll_animal()
    reroll_environment()
    reroll_setting()

def copy_to_clipboard():
    window.clipboard_clear()
    window.clipboard_append(f"Gender: {gender.get()}\nStature: {stature.get()}\nAge: {age.get()}\nSpecies: {species.get()}\nJob: {job.get()}\nMain characteristic: {main.get()}\nFeatures: {feature.get()}\nItem: {item.get()}\nSuper natural ability: {supers.get()}\nAnimal aspect: {animal.get()}\nEnvironment: {environment.get()}\nSetting: {setting.get()}") # what gets copied
    window.update() # keeps the clipboard content after the program is closed

reroll_gender_enabled = True
previous_gender = None

def toggle_reroll_gender():
    global reroll_gender_enabled
    reroll_gender_enabled = not reroll_gender_enabled

def reroll_gender():
    global gender, previous_gender
    if reroll_gender_enabled:
        gender.set(str(random.choice(genderlist)))

def reroll_stature():
    global stature
    stature.set(str(random.choice(staturelist)))    

def reroll_age():   
    global age
    age.set(str(random.choice(agelist)))

def reroll_species():
    global species
    species.set(str(random.choice(specieslist)))

def reroll_job():
    global job
    job.set(str(random.choice(joblist)))

def reroll_main():
    global main
    main.set(str(random.choice(mainlist)))

def reroll_feature():
    global feature
    feature.set(str(random.choice(featurelist)))

def reroll_item():
    global item
    item.set(str(random.choice(itemlist)))

def reroll_supers():
    global supers
    supers.set(str(random.choice(superslist)))

def reroll_animal():
    global animal
    animal.set(str(random.choice(animallist)))

def reroll_environment():
    global environment
    environment.set(str(random.choice(environmentlist)))

def reroll_setting():
    global setting
    setting.set(str(random.choice(settinglist)))


# Window GUI


window = Tk()
window.title("Character randomizer")
icon = PhotoImage(file="icon.png")
window.iconphoto(True, icon)
window.resizable(False, False)
window.config(background="#202020") 
window.geometry("800x1000")

window.option_add("*Font", "Corbel 20") 
window.option_add("*Foreground", "#FFFFFF") 
window.option_add("*Background", "#202020")
window.option_add("*width", "20")
window.option_add("*anchor", "w")

stature = StringVar()
age = StringVar()
gender = StringVar()
species = StringVar()
job = StringVar()
main = StringVar()
feature = StringVar()
item = StringVar()
supers = StringVar()
animal = StringVar()
environment = StringVar()
setting = StringVar()

randomize() # randomizes everything on opening the program

# categories and results

button = Checkbutton(window, command=toggle_reroll_gender, bg="#353535", font=("Corbel", 12), anchor="e", width=1)
button.grid(row=1, column=1, sticky="e")
button = Button(window, text="Reroll", bg="#353535", font=("Corbel", 12), anchor="center", width=5)
button.config(command=reroll_gender)
button.grid(row=1, column=2, padx=5, pady=10, sticky="w")
label1 = Label(window, text="Gender Exp.", font=("Corbel", 20, "bold"), anchor="center").grid(row=1, column=3, padx=20, pady=1, sticky="w")
label2 = Label(window, textvariable=gender, fg="#9ADCFF").grid(row=1, column=4, sticky="w")


label3 = Label(window, text="Stature", font=("Corbel", 20, "bold"), anchor="center").grid(row=2, column=3, padx=20, pady=1)
label4 = Label(window, textvariable=stature, fg="#9ADCFF").grid(row=2, column=4, sticky="w")
button = Button(window, text="Reroll", bg="#353535", font=("Corbel", 12), anchor="center", width=5)
button.config(command=reroll_stature)
button.grid(row=2, column=2, padx=5, pady=10, sticky="w")

label5 = Label(window, text="Age", font=("Corbel", 20, "bold"), anchor="center").grid(row=3, column=3, padx=20, pady=1)
label6 = Label(window, textvariable=age, fg="#9ADCFF").grid(row=3, column=4, sticky="w")
button = Button(window, text="Reroll", bg="#353535", font=("Corbel", 12), anchor="center", width=5)
button.config(command=reroll_age)
button.grid(row=3, column=2, padx=5, pady=10, sticky="w")

label7 = Label(window, text="Species", font=("Corbel", 20, "bold"), anchor="center").grid(row=4, column=3, padx=20, pady=1)
label8 = Label(window, textvariable=species, fg="#9ADCFF").grid(row=4, column=4, sticky="w")
button = Button(window, text="Reroll", bg="#353535", font=("Corbel", 12), anchor="center", width=5)
button.config(command=reroll_species)
button.grid(row=4, column=2, padx=5, pady=10, sticky="w")

label9 = Label(window, text="Job or title", font=("Corbel", 20, "bold"), anchor="center").grid(row=5, column=3, padx=20, pady=1)
label10 = Label(window, textvariable=job, fg="#9ADCFF").grid(row=5, column=4, sticky="w")
button = Button(window, text="Reroll", bg="#353535", font=("Corbel", 12), anchor="center", width=5)
button.config(command=reroll_job)
button.grid(row=5, column=2, padx=5, pady=10, sticky="w")

label11 = Label(window, text="Main characteristic", font=("Corbel", 20, "bold"), anchor="center").grid(row=6, column=3, padx=20, pady=1)
label12 = Label(window, textvariable=main, fg="#9ADCFF").grid(row=6, column=4, sticky="w")
button = Button(window, text="Reroll", bg="#353535", font=("Corbel", 12), anchor="center", width=5)
button.config(command=reroll_main)
button.grid(row=6, column=2, padx=5, pady=10, sticky="w")

label13 = Label(window, text="Features", font=("Corbel", 20, "bold"), anchor="center").grid(row=7, column=3, padx=20, pady=1)
label14 = Label(window, textvariable=feature, fg="#9ADCFF").grid(row=7, column=4, sticky="w")
button = Button(window, text="Reroll", bg="#353535", font=("Corbel", 12), anchor="center", width=5)
button.config(command=reroll_feature)
button.grid(row=7, column=2, padx=5, pady=10, sticky="w")

label15 = Label(window, text="Item", font=("Corbel", 20, "bold"), anchor="center").grid(row=8, column=3, padx=20, pady=1)
label16 = Label(window, textvariable=item, fg="#9ADCFF").grid(row=8, column=4, sticky="w")
button = Button(window, text="Reroll", bg="#353535", font=("Corbel", 12), anchor="center", width=5)
button.config(command=reroll_item)
button.grid(row=8, column=2, padx=5, pady=10, sticky="w")

label17 = Label(window, text="Super natural ability", font=("Corbel", 20, "bold"), anchor="center").grid(row=9, column=3, padx=20, pady=1)
label18 = Label(window, textvariable=supers, fg="#9ADCFF").grid(row=9, column=4, sticky="w")
button = Button(window, text="Reroll", bg="#353535", font=("Corbel", 12), anchor="center", width=5)
button.config(command=reroll_supers)
button.grid(row=9, column=2, padx=5, pady=10, sticky="w")

label19 = Label(window, text="Animal aspect", font=("Corbel", 20, "bold"), anchor="center").grid(row=10, column=3, padx=20, pady=1)
label20 = Label(window, textvariable=animal, fg="#9ADCFF").grid(row=10, column=4, sticky="w")
button = Button(window, text="Reroll", bg="#353535", font=("Corbel", 12), anchor="center", width=5)
button.config(command=reroll_animal)
button.grid(row=10, column=2, padx=5, pady=10, sticky="w")

label21 = Label(window, text="Environment", font=("Corbel", 20, "bold"), anchor="center").grid(row=11, column=3, padx=20, pady=1)
label22 = Label(window, textvariable=environment, fg="#9ADCFF").grid(row=11, column=4, sticky="w")
button = Button(window, text="Reroll", bg="#353535", font=("Corbel", 12), anchor="center", width=5)
button.config(command=reroll_environment)
button.grid(row=11, column=2, padx=5, pady=10, sticky="w")

label23 = Label(window, text="Setting", font=("Corbel", 20, "bold"), anchor="center").grid(row=12, column=3, padx=20, pady=1)
label24 = Label(window, textvariable=setting, fg="#9ADCFF").grid(row=12, column=4, sticky="w")
button = Button(window, text="Reroll", bg="#353535", font=("Corbel", 12), anchor="center", width=5)
button.config(command=reroll_setting)
button.grid(row=12, column=2, padx=5, pady=10, sticky="w")

# reroll button and copy
button = Button(window, text="Randomize!", bg="#43AFD3", fg="#1C1C1C", anchor="center", width=40)
button.config(command=randomize)
button.place(relx=0.5, y=800, anchor="center")

button = Button(window, text="copy to clipboard", bg="#437DD3", fg="#1C1C1C", anchor="center", width=40)
button.config(command=copy_to_clipboard)
button.place(relx=0.5, y=900, anchor="center")

window.mainloop()