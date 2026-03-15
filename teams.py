from pyscript import document

def team_checker(event):
    # 1. OUTPUT BOX --> CHECKS THE DISPLAY OF THE CODE
    output = document.getElementById("display")
    team_img = document.getElementById("team_img")

    # EMPTIES THE DISPLAYS (BOTH THE ONE FOR THE MESSAGE AND IMAGE)
    output.innerText = ""
    team_img.style.display = "none"

    # 2. CHECK IF RADIO ELEMENTS WERE CHECKED --> REGISTRATION AND CLEARANCE
    reg_input = document.querySelector('input[name="reg"]:checked')
    clr_input = document.querySelector('input[name="clr"]:checked')

    # 3. CHECK IF RADIO ELEMENTS ARE UNCLICKED --> REGISTRATION AND CLEARANCE
    if not reg_input or not clr_input:
        output.innerText = "⚠️ Uh oh! Please answer all questions before checking your team!"
        return

    # 4. CHECK THE DISPLAY INPUTS OF OTHER ELEMENTS
    registration = reg_input.value
    clearance = clr_input.value
    grade = int(document.getElementById("level").value)
    section = document.getElementById("section").value

    # 5. CHECKS THE USER'S INTRAMURALS TEAM
    if registration == "yes":
        if clearance == "yes":
            # IF THE USER IS GRADE 7 OR 10
            if grade == 7 or grade == 10:
                if section == "Emerald":
                    output.innerText = "💚 Welcome to the Green Hornets!"
                    team_img.src = "green_hornets.png"
                    team_img.style.display = "block" # "block" means it will display the logo at the the bottom of the container
                elif section == "Ruby":
                    output.innerText = "💛 Welcome to the Yellow Tigers!"
                    team_img.src = "yellow_tigers.png"
                    team_img.style.display = "block"
                else:
                    output.innerText = "⚠️ Uh oh! Please select a valid JHS section (Emerald/Ruby)."
                    team_img.src = ""
                    team_img.style.display = "none" # "none" means it will display nothing at the the bottom of the container
                    
            # IF THE USER IS GRADE 8 OR 9
            elif grade == 8 or grade == 9:
                if section == "Emerald":
                    output.innerText = "❤️ Welcome to the Red Bulldogs!"
                    team_img.src = "red_bulldogs.png"
                    team_img.style.display = "block"
                elif section == "Ruby":
                    output.innerText = "💙 Welcome to the Blue Bears!"
                    team_img.src = "blue_bears.png"
                    team_img.style.display = "block"
                else:
                    output.innerText = "⚠️ Uh oh! Please select a valid JHS section (Emerald/Ruby)."
                    team_img.src = ""
                    team_img.style.display = "none"
            
            # IF THE USER IS GRADE 11
            elif grade == 11:
                if section == "Amorsolo":
                    output.innerText = "❤️ Welcome to the Red Bulldogs!"
                    team_img.src = "red_bulldogs.png"
                    team_img.style.display = "block"
                elif section == "Luna":
                    output.innerText = "💙 Welcome to the Blue Bears!"
                    team_img.src = "blue_bears.png"
                    team_img.style.display = "block"
                else:
                    output.innerText = "⚠️ Uh oh! Please select a valid Grade 11 section (Amorsolo/Luna)."
                    team_img.src = ""
                    team_img.style.display = "none"

            # IF THE USER IS GRADE 12
            elif grade == 12:
                if section == "Jose":
                    output.innerText = "💚 Welcome to the Green Hornets!"
                    team_img.src = "green_hornets.png"
                    team_img.style.display = "block"
                elif section == "Tinio":
                    output.innerText = "💛 Welcome to the Yellow Tigers!"
                    team_img.src = "yellow_tigers.png"
                    team_img.style.display = "block"
                else:
                    output.innerText = "⚠️ Uh oh! Please select a valid Grade 12 section (Jose/Tinio)."
                    team_img.src = ""
                    team_img.style.display = "none"
        
        else:
            # TRIGGERED WHEN THE CLEARANCE IS MARKED AS "NO"
            output.innerText = "⚠️ Oh no! Please secure a medical clearance first!"
            team_img.src = ""
            team_img.style.display = "none"
    else:
        # TRIGGERED WHEN THE REGISTRATION IS MARKED AS "NO"
        output.innerText = "⚠️ oh no! Please ensure to register first!"
        team_img.src = ""
        team_img.style.display = "none"