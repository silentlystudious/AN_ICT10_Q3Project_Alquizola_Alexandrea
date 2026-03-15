from pyscript import document

def classmate_loop(event):
    # 1. DICTIONARY FOR INTRAMURALS PLAYERS USING MY CLASSMATES' NAMES
    # Note: Since the code is under an "ol" in the HTML files, the list will be ordered, meaning "Alquizola, Alexandrea" will go first!
    obmc_classmates = [
        "Alquizola, Alexandrea",
        "Ang, Angelo",
        "Bungay, Janine",
        "Davis, Carl",
        "Dimabuyu, Ryan",
        "Dizon, Sophia",
        "Domingo, Marko",
        "Elechosa, Sharlette",
        "Gatpolintan, Alysia",
        "Layug, Riz",
        "Llanos Dee, Brillance",
        "Manalansan, Kaylie",
        "Manaloto, Zoe",
        "Mapile, Dania",
        "Marquez, Joaquin",
        "Masa, Elijah",
        "Mendoza, Kobe", 
        "Mendoza, Lara",
        "Nygard, Evan",
        "Orfinada, Jacob",
        "Otsuru, Ayumi",
        "Pan, Christophe",
        "Pangilinan, Alan",
        "Santos, Sheena",
        "Soberano, Gonzi",
        "Ubaldo, Cassandra",
        "Velasco, Mhianne"]

    # 2. PLAYER LIST VARIABLE
    obmc_list = document.getElementById("obmc_class") # This code will acquire the variable that stores my list from the HTML file
    obmc_list.innerHTML = "" # Before clicking the button from the HTML file, this code will empty the list upon opening the page

    # 3. PYTHON LOOP --> THE USER CANNOT CHANGE IT EVEN WHEN CLICKING THE BUTTON AGAIN
    for name in obmc_classmates:
        new_name = document.createElement("li")
        new_name.className = "list-group-item"
        new_name.textContent = name
        obmc_list.appendChild(new_name)