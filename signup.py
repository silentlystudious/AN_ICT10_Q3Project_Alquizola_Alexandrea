from pyscript import document, window
import asyncio

async def create_username(event):
    # 1. INPUT HANDLING --> CHECKS THE LOCATION OF EACH VARIABLE FROM THE HTML FILE
    username_input = document.querySelector("#username")
    password_input = document.querySelector("#password")
    email_input = document.querySelector("#email")
    msg_output = document.querySelector("#msg")
    btn = document.querySelector("#btn")

    # 2. CHECK THE VALUE FROM THE INPUTS
    username = username_input.value
    password = password_input.value
    email = email_input.value

    # 3. CHECKS THE USER'S USERNAME AND INPUT
    if not username and not email:
        msg_output.innerText = "⚠️ Please enter a valid username and email!"
    elif not username:
        msg_output.innerText = "⚠️ Please enter a valid username!"
    elif not email:
        msg_output.innerText = "⚠️ Please enter a valid email!"
    elif len(password) < 8:
        msg_output.innerText = "⚠️ Please enter an 8-digit password!"
    else:
        # 4. SUCCESS ON CREATING THE ACCOUNT
        msg_output.innerText = f"☑️ Account created for {username}!\n😊 You may now log in using your credentials!"
        btn.disabled = True
        btn.innerText = "⌛ Successful! Please wait..."

        # 5. CLEARS THE INPUTS AFTER SUBMITTING
        username_input.value = ""
        email_input.value = ""
        password_input.value = ""

        # 6. BUTTON COOLDOWN AND RELOAD WEBSITE
        await asyncio.sleep(5) # After the user submits, the webpage will reload after five seconds :)
        window.location.reload() # The reason I included this code is because I wanted the interface to mimic a real log-in site!