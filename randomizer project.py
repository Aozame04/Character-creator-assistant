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
    itemlist = [string.strip() for string in lines[6].removeprefix("Item: ").split(',')]
    superslist = [string.strip() for string in lines[7].removeprefix("Super natural ability: ").split(',')]
    animallist = [string.strip() for string in lines[8].removeprefix("Animal aspect: ").split(',')]
    envirolist = [string.strip() for string in lines[9].removeprefix("Environment: ").split(',')]
    settinglist = [string.strip() for string in lines[10].removeprefix("Setting: ").split(',')]
    extralist = (joblist + mainlist + itemlist + superslist + animallist)

def randomize():
    global gender, stature, age, species, job, main, item, supers, animal, enviro, setting
    if reroll_gender_enabled:
        gender.set(str(random.choice(genderlist)))
    if reroll_stature_enabled:
        stature.set(str(random.choice(staturelist))) 
    if reroll_age_enabled:
        age.set(str(random.choice(agelist)))         
    if reroll_species_enabled:
        species.set(str(random.choice(specieslist))) 
    if reroll_job_enabled:
        job.set(str(random.choice(joblist))) 
    if reroll_main_enabled:
        main.set(str(random.choice(mainlist))) 
    if reroll_item_enabled:
        item.set(str(random.choice(itemlist))) 
    if reroll_supers_enabled:
        supers.set(str(random.choice(superslist))) 
    if reroll_animal_enabled:
        animal.set(str(random.choice(animallist))) 
    if reroll_enviro_enabled:
        enviro.set(str(random.choice(envirolist))) 
    if reroll_setting_enabled:
        setting.set(str(random.choice(settinglist))) 
    if reroll_extra_enabled:
        extra.set(str(random.choice(extralist)))

def copy_to_clipboard():
    window.clipboard_clear()

    clipboard = (
        f"Gender: {gender.get()}\n"
        f"Stature: {stature.get()}\n"
        f"Age: {age.get()}\n"
        f"Species: {species.get()}\n"
        f"Job: {job.get()}\n"
        f"Main characteristic: {main.get()}\n"
        f"Item: {item.get()}\n"
        f"Super natural ability: {supers.get()}\n"
        f"Animal aspect: {animal.get()}\n"
        f"Environment: {enviro.get()}\n"
        f"Setting: {setting.get()}\n"
        f"Extra: {extra.get()}")

    window.clipboard_append(clipboard)
    window.update() # keeps the clipboard content after the program is closed

# all of the categories commands

reroll_gender_enabled = True
previous_gender = None
new_gender = None

def toggle_reroll_gender():
    global reroll_gender_enabled
    reroll_gender_enabled = not reroll_gender_enabled

    if reroll_gender_enabled:
        genderlabel2.config(fg="#9ADCFF")
        genderlabel1.config(fg="white")
    else:
        genderlabel2.config(fg="gray")
        genderlabel1.config(fg="gray")

def reroll_gender():
    global gender, previous_gender
    if reroll_gender_enabled:
        available_gender_s = list(set(genderlist))

        if previous_gender in available_gender_s:
            available_gender_s.remove(previous_gender)

        if available_gender_s:
            new_gender = random.choice(available_gender_s)
            previous_gender = new_gender
            gender.set(str(new_gender))

reroll_stature_enabled = True
previous_stature = None
new_stature = None

def toggle_reroll_stature():
    global reroll_stature_enabled
    reroll_stature_enabled = not reroll_stature_enabled

    if reroll_stature_enabled:
        staturelabel2.config(fg="#9ADCFF")
        staturelabel1.config(fg="white")
    else:
        staturelabel2.config(fg="gray")
        staturelabel1.config(fg="gray")

def reroll_stature():
    global stature, previous_stature
    if reroll_stature_enabled:
        available_stature_s = list(set(staturelist))

        if previous_stature in available_stature_s:
            available_stature_s.remove(previous_stature)

        if available_stature_s:
            new_stature = random.choice(available_stature_s)
            previous_stature = new_stature
            stature.set(str(new_stature))

reroll_age_enabled = True
previous_age = None
new_age = None

def toggle_reroll_age():
    global reroll_age_enabled
    reroll_age_enabled = not reroll_age_enabled

    if reroll_age_enabled:
        agelabel2.config(fg="#9ADCFF")
        agelabel1.config(fg="white")
    else:
        agelabel2.config(fg="gray")
        agelabel1.config(fg="gray")

def reroll_age():
    global age, previous_age
    if reroll_age_enabled:
        available_age_s = list(set(agelist))

        if previous_age in available_age_s:
            available_age_s.remove(previous_age)

        if available_age_s:
            new_age = random.choice(available_age_s)
            previous_age = new_age
            age.set(str(new_age))

reroll_species_enabled = True
previous_species = None
new_species = None

def toggle_reroll_species():
    global reroll_species_enabled
    reroll_species_enabled = not reroll_species_enabled

    if reroll_species_enabled:
        specieslabel2.config(fg="#9ADCFF")
        specieslabel1.config(fg="white")
    else:
        specieslabel2.config(fg="gray")
        specieslabel1.config(fg="gray")

def reroll_species():
    global species, previous_species
    if reroll_species_enabled:
        available_species_s = list(set(specieslist))

        if previous_species in available_species_s:
            available_species_s.remove(previous_species)

        if available_species_s:
            new_species = random.choice(available_species_s)
            previous_species = new_species
            species.set(str(new_species))

reroll_job_enabled = True
previous_job = None
new_job = None

def toggle_reroll_job():
    global reroll_job_enabled
    reroll_job_enabled = not reroll_job_enabled

    if reroll_job_enabled:
        joblabel2.config(fg="#9ADCFF")
        joblabel1.config(fg="white")
    else:
        joblabel2.config(fg="gray")
        joblabel1.config(fg="gray")

def reroll_job():
    global job, previous_job
    if reroll_job_enabled:
        available_job_s = list(set(joblist))

        if previous_job in available_job_s:
            available_job_s.remove(previous_job)

        if available_job_s:
            new_job = random.choice(available_job_s)
            previous_job = new_job
            job.set(str(new_job))

reroll_main_enabled = True
previous_main = None
new_main = None

def toggle_reroll_main():
    global reroll_main_enabled
    reroll_main_enabled = not reroll_main_enabled

    if reroll_main_enabled:
        mainlabel2.config(fg="#9ADCFF")
        mainlabel1.config(fg="white")
    else:
        mainlabel2.config(fg="gray")
        mainlabel1.config(fg="gray")

def reroll_main():
    global main, previous_main
    if reroll_main_enabled:
        available_main_s = list(set(mainlist))

        if previous_main in available_main_s:
            available_main_s.remove(previous_main)

        if available_main_s:
            new_main = random.choice(available_main_s)
            previous_main = new_main
            main.set(str(new_main))

reroll_item_enabled = True
previous_item = None
new_item = None

def toggle_reroll_item():
    global reroll_item_enabled
    reroll_item_enabled = not reroll_item_enabled

    if reroll_item_enabled:
        itemlabel2.config(fg="#9ADCFF")
        itemlabel1.config(fg="white")
    else:
        itemlabel2.config(fg="gray")
        itemlabel1.config(fg="gray")

def reroll_item():
    global item, previous_item
    if reroll_item_enabled:
        available_item_s = list(set(itemlist))

        if previous_item in available_item_s:
            available_item_s.remove(previous_item)

        if available_item_s:
            new_item = random.choice(available_item_s)
            previous_item = new_item
            item.set(str(new_item))

reroll_supers_enabled = True
previous_supers = None
new_supers = None

def toggle_reroll_supers():
    global reroll_supers_enabled
    reroll_supers_enabled = not reroll_supers_enabled

    if reroll_supers_enabled:
        superslabel2.config(fg="#9ADCFF")
        superslabel1.config(fg="white")
    else:
        superslabel2.config(fg="gray")
        superslabel1.config(fg="gray")

def reroll_supers():
    global supers, previous_supers
    if reroll_supers_enabled:
        available_supers_s = list(set(superslist))

        if previous_supers in available_supers_s:
            available_supers_s.remove(previous_supers)

        if available_supers_s:
            new_supers = random.choice(available_supers_s)
            previous_supers = new_supers
            supers.set(str(new_supers))

reroll_animal_enabled = True
previous_animal = None
new_animal = None

def toggle_reroll_animal():
    global reroll_animal_enabled
    reroll_animal_enabled = not reroll_animal_enabled

    if reroll_animal_enabled:
        animallabel2.config(fg="#9ADCFF")
        animallabel1.config(fg="white")
    else:
        animallabel2.config(fg="gray")
        animallabel1.config(fg="gray")

def reroll_animal():
    global animal, previous_animal
    if reroll_animal_enabled:
        available_animal_s = list(set(animallist))

        if previous_animal in available_animal_s:
            available_animal_s.remove(previous_animal)

        if available_animal_s:
            new_animal = random.choice(available_animal_s)
            previous_animal = new_animal
            animal.set(str(new_animal))

reroll_enviro_enabled = True
previous_enviro = None
new_enviro = None

def toggle_reroll_enviro():
    global reroll_enviro_enabled
    reroll_enviro_enabled = not reroll_enviro_enabled

    if reroll_enviro_enabled:
        envirolabel2.config(fg="#9ADCFF")
        envirolabel1.config(fg="white")
    else:
        envirolabel2.config(fg="gray")
        envirolabel1.config(fg="gray")

def reroll_enviro():
    global enviro, previous_enviro
    if reroll_enviro_enabled:
        available_enviro_s = list(set(envirolist))

        if previous_enviro in available_enviro_s:
            available_enviro_s.remove(previous_enviro)

        if available_enviro_s:
            new_enviro = random.choice(available_enviro_s)
            previous_enviro = new_enviro
            enviro.set(str(new_enviro))

reroll_setting_enabled = True
previous_setting = None
new_setting = None

def toggle_reroll_setting():
    global reroll_setting_enabled
    reroll_setting_enabled = not reroll_setting_enabled

    if reroll_setting_enabled:
        settinglabel2.config(fg="#9ADCFF")
        settinglabel1.config(fg="white")
    else:
        settinglabel2.config(fg="gray")
        settinglabel1.config(fg="gray")

def reroll_setting():
    global setting, previous_setting
    if reroll_setting_enabled:
        available_setting_s = list(set(settinglist))

        if previous_setting in available_setting_s:
            available_setting_s.remove(previous_setting)

        if available_setting_s:
            new_setting = random.choice(available_setting_s)
            previous_setting = new_setting
            setting.set(str(new_setting))

reroll_extra_enabled = True
previous_extra = None
new_extra = None

def toggle_reroll_extra():
    global reroll_extra_enabled
    reroll_extra_enabled = not reroll_extra_enabled

    if reroll_extra_enabled:
        extralabel2.config(fg="#9ADCFF")
        extralabel1.config(fg="white")
    else:
        extralabel2.config(fg="gray")
        extralabel1.config(fg="gray")

def reroll_extra():
    global extra, previous_extra
    if reroll_extra_enabled:
        available_extra_s = list(set(extralist))

        if previous_extra in available_extra_s:
            available_extra_s.remove(previous_extra)

        if available_extra_s:
            new_extra = random.choice(available_extra_s)
            previous_extra = new_extra
            extra.set(str(new_extra))


# Window GUI


window = Tk()
window.title("Character randomizer")
icon = PhotoImage(file="icon.png")
window.iconphoto(True, icon)
window.resizable(False, False)
window.config(background="#202020") 
window.geometry("640x650")

window.option_add("*Font", "Corbel 20") 
window.option_add("*Foreground", "white") 
window.option_add("*Background", "#202020")
window.option_add("*width", "15")
window.option_add("*anchor", "w")

gender = StringVar()
stature = StringVar()
age = StringVar()
species = StringVar()
job = StringVar()
main = StringVar()
item = StringVar()
supers = StringVar()
animal = StringVar()
enviro = StringVar()
setting = StringVar()
extra = StringVar()

randomize() # randomizes everything on opening the program

# GUI for categories and results

button = Checkbutton(window, command=toggle_reroll_gender, bg="#353535", font=("Corbel", 12), anchor="e", width=1)
button.grid(row=1, column=1, sticky="e")
genderbutton = Button(window, text="Reroll", bg="#353535", font=("Corbel", 12), anchor="center", width=5)
genderbutton.config(command=reroll_gender)
genderbutton.grid(row=1, column=2, padx=2, pady=5, sticky="w")
genderlabel1 = Label(window, text="Gender expr.", font=("Corbel", 20, "bold"), anchor="center", fg="white", bg="#353535")
genderlabel1.grid(row=1, column=3, padx=2, pady=1, sticky="w")
genderlabel2 = Label(window, textvariable=gender, fg="#9ADCFF")
genderlabel2.grid(row=1, column=4, sticky="w")

button = Checkbutton(window, command=toggle_reroll_stature, bg="#353535", font=("Corbel", 12), anchor="e", width=1)
button.grid(row=2, column=1, sticky="e")
staturebutton = Button(window, text="Reroll", bg="#353535", font=("Corbel", 12), anchor="center", width=5)
staturebutton.config(command=reroll_stature)
staturebutton.grid(row=2, column=2, padx=2, pady=5, sticky="w")
staturelabel1 = Label(window, text="Stature", font=("Corbel", 20, "bold"), anchor="center", fg="white", bg="#353535")
staturelabel1.grid(row=2, column=3, padx=2, pady=1, sticky="w")
staturelabel2 = Label(window, textvariable=stature, fg="#9ADCFF")
staturelabel2.grid(row=2, column=4, sticky="w")

button = Checkbutton(window, command=toggle_reroll_age, bg="#353535", font=("Corbel", 12), anchor="e", width=1)
button.grid(row=3, column=1, sticky="e")
agebutton = Button(window, text="Reroll", bg="#353535", font=("Corbel", 12), anchor="center", width=5)
agebutton.config(command=reroll_age)
agebutton.grid(row=3, column=2, padx=2, pady=5, sticky="w")
agelabel1 = Label(window, text="Age", font=("Corbel", 20, "bold"), anchor="center", fg="white", bg="#353535")
agelabel1.grid(row=3, column=3, padx=2, pady=1, sticky="w")
agelabel2 = Label(window, textvariable=age, fg="#9ADCFF")
agelabel2.grid(row=3, column=4, sticky="w")

button = Checkbutton(window, command=toggle_reroll_species, bg="#353535", font=("Corbel", 12), anchor="e", width=1)
button.grid(row=4, column=1, sticky="e")
speciesbutton = Button(window, text="Reroll", bg="#353535", font=("Corbel", 12), anchor="center", width=5)
speciesbutton.config(command=reroll_species)
speciesbutton.grid(row=4, column=2, padx=2, pady=5, sticky="w")
specieslabel1 = Label(window, text="Species", font=("Corbel", 20, "bold"), anchor="center", fg="white", bg="#353535")
specieslabel1.grid(row=4, column=3, padx=2, pady=1, sticky="w")
specieslabel2 = Label(window, textvariable=species, fg="#9ADCFF")
specieslabel2.grid(row=4, column=4, sticky="w")

button = Checkbutton(window, command=toggle_reroll_job, bg="#353535", font=("Corbel", 12), anchor="e", width=1)
button.grid(row=5, column=1, sticky="e")
jobbutton = Button(window, text="Reroll", bg="#353535", font=("Corbel", 12), anchor="center", width=5)
jobbutton.config(command=reroll_job)
jobbutton.grid(row=5, column=2, padx=2, pady=5, sticky="w")
joblabel1 = Label(window, text="Job", font=("Corbel", 20, "bold"), anchor="center", fg="white", bg="#353535")
joblabel1.grid(row=5, column=3, padx=2, pady=1, sticky="w")
joblabel2 = Label(window, textvariable=job, fg="#9ADCFF")
joblabel2.grid(row=5, column=4, sticky="w")

button = Checkbutton(window, command=toggle_reroll_main, bg="#353535", font=("Corbel", 12), anchor="e", width=1)
button.grid(row=6, column=1, sticky="e")
mainbutton = Button(window, text="Reroll", bg="#353535", font=("Corbel", 12), anchor="center", width=5)
mainbutton.config(command=reroll_main)
mainbutton.grid(row=6, column=2, padx=2, pady=5, sticky="w")
mainlabel1 = Label(window, text="Main", font=("Corbel", 20, "bold"), anchor="center", fg="white", bg="#353535")
mainlabel1.grid(row=6, column=3, padx=2, pady=1, sticky="w")
mainlabel2 = Label(window, textvariable=main, fg="#9ADCFF")
mainlabel2.grid(row=6, column=4, sticky="w")

button = Checkbutton(window, command=toggle_reroll_item, bg="#353535", font=("Corbel", 12), anchor="e", width=1)
button.grid(row=7, column=1, sticky="e")
itembutton = Button(window, text="Reroll", bg="#353535", font=("Corbel", 12), anchor="center", width=5)
itembutton.config(command=reroll_item)
itembutton.grid(row=7, column=2, padx=2, pady=5, sticky="w")
itemlabel1 = Label(window, text="Item or items", font=("Corbel", 20, "bold"), anchor="center", fg="white", bg="#353535")
itemlabel1.grid(row=7, column=3, padx=2, pady=1, sticky="w")
itemlabel2 = Label(window, textvariable=item, fg="#9ADCFF")
itemlabel2.grid(row=7, column=4, sticky="w")

button = Checkbutton(window, command=toggle_reroll_supers, bg="#353535", font=("Corbel", 12), anchor="e", width=1)
button.grid(row=8, column=1, sticky="e")
supersbutton = Button(window, text="Reroll", bg="#353535", font=("Corbel", 12), anchor="center", width=5)
supersbutton.config(command=reroll_supers)
supersbutton.grid(row=8, column=2, padx=2, pady=5, sticky="w")
superslabel1 = Label(window, text="Super ability", font=("Corbel", 20, "bold"), anchor="center", fg="white", bg="#353535")
superslabel1.grid(row=8, column=3, padx=2, pady=1, sticky="w")
superslabel2 = Label(window, textvariable=supers, fg="#9ADCFF")
superslabel2.grid(row=8, column=4, sticky="w")

button = Checkbutton(window, command=toggle_reroll_animal, bg="#353535", font=("Corbel", 12), anchor="e", width=1)
button.grid(row=9, column=1, sticky="e")
animalbutton = Button(window, text="Reroll", bg="#353535", font=("Corbel", 12), anchor="center", width=5)
animalbutton.config(command=reroll_animal)
animalbutton.grid(row=9, column=2, padx=2, pady=5, sticky="w")
animallabel1 = Label(window, text="Animal Aspect", font=("Corbel", 20, "bold"), anchor="center", fg="white", bg="#353535")
animallabel1.grid(row=9, column=3, padx=2, pady=1, sticky="w")
animallabel2 = Label(window, textvariable=animal, fg="#9ADCFF")
animallabel2.grid(row=9, column=4, sticky="w")

button = Checkbutton(window, command=toggle_reroll_enviro, bg="#353535", font=("Corbel", 12), anchor="e", width=1)
button.grid(row=10, column=1, sticky="e")
envirobutton = Button(window, text="Reroll", bg="#353535", font=("Corbel", 12), anchor="center", width=5)
envirobutton.config(command=reroll_enviro)
envirobutton.grid(row=10, column=2, padx=2, pady=5, sticky="w")
envirolabel1 = Label(window, text="Enviroment", font=("Corbel", 20, "bold"), anchor="center", fg="white", bg="#353535")
envirolabel1.grid(row=10, column=3, padx=2, pady=1, sticky="w")
envirolabel2 = Label(window, textvariable=enviro, fg="#9ADCFF")
envirolabel2.grid(row=10, column=4, sticky="w")

button = Checkbutton(window, command=toggle_reroll_setting, bg="#353535", font=("Corbel", 12), anchor="e", width=1)
button.grid(row=11, column=1, sticky="e")
settingbutton = Button(window, text="Reroll", bg="#353535", font=("Corbel", 12), anchor="center", width=5)
settingbutton.config(command=reroll_setting)
settingbutton.grid(row=11, column=2, padx=2, pady=5, sticky="w")
settinglabel1 = Label(window, text="Setting", font=("Corbel", 20, "bold"), anchor="center", fg="white", bg="#353535")
settinglabel1.grid(row=11, column=3, padx=2, pady=1, sticky="w")
settinglabel2 = Label(window, textvariable=setting, fg="#9ADCFF")
settinglabel2.grid(row=11, column=4, sticky="w")

# extra

button = Checkbutton(window, command=toggle_reroll_extra, bg="#353535", font=("Corbel", 12), anchor="e", width=1)
button.grid(row=12, column=1, sticky="e")
extrabutton = Button(window, text="Reroll", bg="#353535", font=("Corbel", 12), anchor="center", width=5)
extrabutton.config(command=reroll_extra)
extrabutton.grid(row=12, column=2, padx=2, pady=5, sticky="w")
extralabel1 = Label(window, text="Extra", font=("Corbel", 20, "bold"), anchor="center", fg="white", bg="#353535")
extralabel1.grid(row=12, column=3, padx=2, pady=1, sticky="w")
extralabel2 = Label(window, textvariable=extra, fg="#9ADCFF")
extralabel2.grid(row=12, column=4, sticky="w")

# reroll button and copy
button = Button(window, text="Randomize!", bg="#43AFD3", fg="#1C1C1C", anchor="center", width=41)
button.config(command=randomize)
button.place(relx=0.5, y=550, anchor="center")

button = Button(window, text="copy to clipboard", bg="#437DD3", fg="#1C1C1C", anchor="center", width=41)
button.config(command=copy_to_clipboard)
button.place(relx=0.5, y=615, anchor="center")

window.mainloop()