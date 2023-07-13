import streamlit as st
import requests
import random
import time

st.set_page_config(page_title="PokemonGame", page_icon="https://slackmojis.com/emojis/186-pokeball/download", initial_sidebar_state="expanded")

# Constants
POKEAPI_URL = "https://pokeapi.co/api/v2/pokemon/"
POKEMON_LIST = ["bulbasaur", "charmander", "squirtle", "pikachu", "chikorita", "cyndaquil",
                "totodile", "treecko", "torchic", "mudkip", "turtwig", "chimchar", "piplup"]



# Helper function to retrieve Pokemon data from PokeAPI
def get_pokemon_data(name):
    response = requests.get(f"{POKEAPI_URL}{name}").json()
    return {
        "name": response["name"],
        "image_url": response["sprites"]["front_default"],
        "type": response["types"][0]["type"]["name"],
        "hp": response["stats"][0]["base_stat"],
        "attack": response["stats"][1]["base_stat"],
        "defense": response["stats"][2]["base_stat"],
        "speed": response["stats"][5]["base_stat"]
    }

def calculate_damage(attacker, defender):
    attack = attacker["attack"]  # The attack value of attacking pokemon
    a_speed = attacker["speed"]  # The speed value of attacking pokemon
    defense = defender["defense"]  # The attack value of defending pokemon
    d_speed = defender["speed"]  # The speed value of defending pokemon
    modifier = random.uniform(0.85, 1.0)  # Apply a random damage modifier between 0.85 and 1.0
    damage = (attack*a_speed*0.01-defense*d_speed*0.01) * modifier
    return int(abs(damage))


# Define the game logic for 1 player mode
def play_1player_mode():
    st.write("Select your Pokemon:")
    player_pokemon = st.selectbox(f"Pokemon", POKEMON_LIST)
    player_pokemon_data = get_pokemon_data(player_pokemon)
    st.image(player_pokemon_data["image_url"])
    st.info(f"{player_pokemon_data['name'].capitalize()} - Type: {player_pokemon_data['type']}, HP: {player_pokemon_data['hp']}, Attack: {player_pokemon_data['attack']}, Defense: {player_pokemon_data['defense']}, Speed: {player_pokemon_data['speed']}")


    #CPU choose a random pokemon
    cpu_pokemon = POKEMON_LIST[random.randrange(len(POKEMON_LIST))]
    cpu_pokemon_data = get_pokemon_data(cpu_pokemon)
    st.image(cpu_pokemon_data["image_url"])
    st.info(f"{cpu_pokemon_data['name'].capitalize()} - Type: {cpu_pokemon_data['type']}, HP: {cpu_pokemon_data['hp']}, Attack: {cpu_pokemon_data['attack']}, Defense: {cpu_pokemon_data['defense']}, Speed: {cpu_pokemon_data['speed']}")

    # Start the battle
    if st.button("Battle Start!"):
        st.session_state["battle_started"] = True

    # Check if the battle has started
    if st.session_state.get("battle_started", False):

        # Randomly select the first attacker
        if random.randint(0,1)==1:
            attacker = player_pokemon_data
            defender = cpu_pokemon_data
            st.write(f"{attacker['name'].capitalize()} for Player attacks {defender['name'].capitalize()} for CPU!")
        else:
            attacker = cpu_pokemon_data
            defender = player_pokemon_data
            st.write(f"{attacker['name'].capitalize()} for CPU attacks {defender['name'].capitalize()} for Player!")

        # Initialize the round count to 1
        round_count = 1


        while attacker['hp']>0 and defender['hp']>0:
            st.header(f"Round {round_count}")
            with st.spinner('Wait for it...'):
                time.sleep(2)
                st.success(f"{attacker['name'].capitalize()} attacks {defender['name'].capitalize()}!")
            defender['hp'] -= calculate_damage(attacker, defender)
            st.write(f"{defender['name'].capitalize()} takes {calculate_damage(attacker, defender)} damage! HP: {defender['hp']}")
            round_count+=1
            if attacker['hp']>0 and defender['hp']>0:
                st.header(f"Round {round_count}")
                with st.spinner('Wait for it...'):
                    time.sleep(2)
                    st.success(f"{defender['name'].capitalize()} attacks {attacker['name'].capitalize()}!")
                attacker['hp'] -= calculate_damage(defender, attacker)
                st.write(f"{attacker['name'].capitalize()} takes {calculate_damage(defender, attacker)} damage! HP: {attacker['hp']}")
                round_count+=1

        if attacker['hp']> defender['hp']:
            st.header(f"{attacker['name'].capitalize()}")
            st.subheader("wins the battle!")
            st.image(attacker["image_url"])
        elif attacker['hp']< defender['hp']:
            st.header(f"{defender['name'].capitalize()}")
            st.subheader("wins the battle!")
            st.image(defender["image_url"])
        else:
            st.write(f"It's a tie!")

# Define the game logic for 2 player mode
def play_2player_mode():
    st.write("Select Player 1's Pokemon:")
    st.sidebar.write("\nPlayer 1's")
    player1_pokemon = st.sidebar.selectbox("Pokemon", POKEMON_LIST, key="player1_pokemon")
    player1_pokemon_data = get_pokemon_data(player1_pokemon)
    st.image(player1_pokemon_data["image_url"])
    st.info(f"{player1_pokemon_data['name'].capitalize()} - Type: {player1_pokemon_data['type']}, HP: {player1_pokemon_data['hp']}, Attack: {player1_pokemon_data['attack']}, Defense: {player1_pokemon_data['defense']}, Speed: {player1_pokemon_data['speed']}")

    st.write("Select Player 2's Pokemon:")
    st.sidebar.write("\nPlayer 2's")
    player2_pokemon = st.sidebar.selectbox("Pokemon", POKEMON_LIST, key="player2_pokemon")
    player2_pokemon_data = get_pokemon_data(player2_pokemon)
    st.image(player2_pokemon_data["image_url"])
    st.info(f"{player2_pokemon_data['name'].capitalize()} - Type: {player2_pokemon_data['type']}, HP: {player2_pokemon_data['hp']}, Attack: {player2_pokemon_data['attack']}, Defense: {player2_pokemon_data['defense']}, Speed: {player2_pokemon_data['speed']}")

    # Start the battle
    if st.button("Start Battle Now!"):
        st.session_state["battle_started"] = True

        # Check if the battle has started
        if st.session_state.get("battle_started", False):
            # Randomly select the first attacker
            if random.randint(0,1)==1:
                attacker = player1_pokemon_data
                defender = player2_pokemon_data
                st.write(f"After a coin flip, Player 1 starts and attacks Player 2's {defender['name'].capitalize()}!\n")
            else:
                attacker = player2_pokemon_data
                defender = player1_pokemon_data
                st.write(f"After a coin flip, Player 2 starts and attacks Player 1's {defender['name'].capitalize()}!\n")

            # Initialize the round count to 1
            round_count = 1

            while attacker['hp']>0 and defender['hp']>0:
                st.header(f"Round {round_count}")
                with st.spinner('Wait for it...'):
                          time.sleep(2)
                          st.success(f"{attacker['name'].capitalize()} attacks {defender['name'].capitalize()}!")
                defender['hp'] -= calculate_damage(attacker, defender)
                st.write(f"{defender['name'].capitalize()} takes {calculate_damage(attacker, defender)} damage! HP: {defender['hp']}")
                round_count+=1
                if attacker['hp']>0 and defender['hp']>0:
                    st.header(f"Round {round_count}")
                    with st.spinner('Wait for it...'):
                          time.sleep(2)
                          st.success(f"{defender['name'].capitalize()} attacks {attacker['name'].capitalize()}!")
                    attacker['hp'] -= calculate_damage(defender, attacker)
                    st.write(f"{attacker['name'].capitalize()} takes {calculate_damage(defender, attacker)} damage! HP: {attacker['hp']}")
                    round_count+=1

            if attacker['hp']> defender['hp']:
                st.header(f"{attacker['name'].capitalize()}")
                st.subheader("wins the battle!")
                st.image(attacker["image_url"])
            elif attacker['hp']< defender['hp']:
                st.header(f"{defender['name'].capitalize()}")
                st.subheader("wins the battle!")
                st.image(defender["image_url"])
            else:
                st.write(f"It's a tie!")


        else:
            st.session_state.get("battle_started", True)



# Define the main function that runs the Streamlit app
def main():
    st.title("Pokemon Battle Game")

    # Select 1 or 2 player mode
    num_players = st.radio("Select number of players", options=['Select Mode', '1 Player Game', '2 Player Game'])

    # Play the game
    if num_players == '1 Player Game':
        expand_1player = st.expander("Single Player Game", expanded=True)
        with expand_1player:
            play_1player_mode()
    elif num_players == '2 Player Game':
        expand_2player = st.expander("Two Players Game", expanded=True)
        with expand_2player:
            play_2player_mode()
    else:
        st.info("Please Select a Game Mode")


if __name__ == "__main__":
    main()
