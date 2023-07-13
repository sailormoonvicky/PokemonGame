# Pokemon Battle Game

<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRR7H1ZMJkVYiKmC_-TxnFh44TRNyPY8H8Sug&usqp=CAU">

Welcome to the Pokemon Battle Game! This Streamlit web application allows users to play a Pokemon battle game in either single-player or two-player mode. This project consists of two applications: one that retrieves data from the Pokemon API and another that retrieves data from a MongoDB database. The applications allow users to play a Pokemon battle game and view rankings based on game results.

## API Game

The API Game application retrieves data from the Pokemon API and allows users to play the Pokemon battle game. The application is deployed at [https://pokemonggameapi.streamlit.app/](https://pokemonggameapi.streamlit.app/).

### Features

- Single Player Mode: Play against the CPU and battle with randomly selected Pokemon.
- Damage Calculation: Calculate the damage inflicted by attacks based on Pokemon stats.
- Round-Based Battles: Engage in battles with multiple rounds until one Pokemon wins.
- Pokemon Data: Retrieve Pokemon data from the Pokemon API.

### Code

The code for the API Game can be found in the [PokeGame_API.py](PokeGame_API.py) file.

### Demo

You can try out the Pokemon Battle Game by visiting the following URL: [https://pokemonggameapi.streamlit.app/](https://pokemonggameapi.streamlit.app/).

## Database Game

The Database Game application retrieves data from a MongoDB database and allows users to play the Pokemon battle game. The application is deployed at [https://pokemongame.streamlit.app/](https://pokemongame.streamlit.app/).

### Features

- Single Player Mode: Play against the CPU and battle with randomly selected Pokemon.
- Two Player Mode: Play against another player and battle with chosen Pokemon.
- MongoDB Integration: Store game data such as wins and losses in a MongoDB database.
- Ranking System: View the leaderboard to see the top-ranked Pokemon based on their game performance.

### Code

The code for the Database Game can be found in the [PokeGame_MongoDB.py](PokeGame_MongoDB.py) file.

### Demo
You can try out the Pokemon Battle Game by visiting the following URL: [https://pokemongame.streamlit.app/](https://pokemongame.streamlit.app/).

## Team and Pokemon Selection

This game has been developed by our team, who have selected 13 Pokemon to feature in the game. The chosen Pokemon are:

- Bulbasaur
- Charmander
- Squirtle
- Pikachu
- Chikorita
- Cyndaquil
- Totodile
- Treecko
- Torchic
- Mudkip
- Turtwig
- Chimchar
- Piplup

These Pokemon were selected based on their popularity and diversity in type and abilities.

## Installation
To run the applications locally, follow these steps:

1. Clone the GitHub repository:
gh repo clone sailormoonvicky/PokemonGame

2. Navigate to the project directory:
cd PokemonGame

3. Install the required dependencies:
pip install -r requirements.txt


## Usage

1. Run the API Game Streamlit app locally:
streamlit run PokeGame_API.py

2. Access the Databese Game app in your web browser at [https://pokemongame.streamlit.app/](https://pokemongame.streamlit.app/).

3. Select the desired game mode: single-player or two-player.

4. Follow the instructions on the web page to play the game. Choose your Pokemon, start the battle, and watch the battle unfold!

## Dependencies

The following Python packages are required to run the Pokemon Battle Game:

- pymongo>=3.11.0
- streamlit>=1.22.0
- requests>=2.28.1
- pandas>=1.4.4

These dependencies can be installed using the `pip install -r requirements.txt` command.


## Contributing

Contributions to the Pokemon Battle Game are welcome! If you encounter any issues or have suggestions for improvements, please create a new issue or submit a pull request.
