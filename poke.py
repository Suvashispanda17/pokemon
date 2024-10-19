import requests 
import getpass as gt 

base_url= " https://pokeapi.co/api/v2"
print(r'''   
      
                
             ____       _                              
            |  _ \ ___ | | _____ _ __ ___   ___  _ __  
            | |_) / _ \| |/ / _ \ '_ ` _ \ / _ \| '_ \ 
            |  __/ (_) |   <  __/ | | | | | (_) | | | |
            |_|   \___/|_|\_\___|_| |_| |_|\___/|_| |_|
                
                
      
       ''')
def poke_info(name):
    url= f"{base_url}/pokemon/{name}"
    reponse= requests.get(url)
    # print(reponse)

    if reponse.status_code == 200:
        # print("data retrieved ")

        poke_data= reponse.json()
        # print(poke_data)
        return poke_data
    else:
        print(f"No Pokemon named : {name}")
        print("                             ----Failed To Retriev Pokemon  Data-----------    ")







password= "Panda"


while True:
    pas = gt.getpass("Password Required: ")
    if password == pas:
        print("Access Granted")
        break  # exit the loop if password is correct
    else:
        print("Access Denied")
        retry = input("Do you want to try again? (yes/no): ")
        if retry.lower() != "yes":
            print("Exiting...")
            exit()


pokemon_name = input("Enter the pokemon name : ")
pokemom = poke_info(pokemon_name)
if pokemom:
    print(f"                     pokemon  name  : {pokemom['name'].capitalize()} ")
    print(f"                     pokemon  id    : {pokemom['id']}")
    print(f"                     pokemon  height: {pokemom['height']}")
    print(f"                     pokemon  weight: {pokemom['weight']} kg.. According to indians 😂")








