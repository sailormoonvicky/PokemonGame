# Pokemon Battle Game

<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRR7H1ZMJkVYiKmC_-TxnFh44TRNyPY8H8Sug&usqp=CAU">

Welcome to the Pokemon Battle Game! This Streamlit web application allows users to play a Pokemon battle game in either single-player or two-player mode. The game data is fetched from the [Pokemon API](https://pokeapi.co/) to provide information about the selected Pokemon.

## Demo

You can try out the Pokemon Battle Game by visiting the following URL: [https://pokemongame.streamlit.app/](https://pokemongame.streamlit.app/)

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

1. Clone the GitHub repository:
gh repo clone sailormoonvicky/PokemonGame

2. Navigate to the project directory:
cd PokemonGame

3. Install the required dependencies:
pip install -r requirements.txt


## Usage

1. Run the Streamlit app locally:
streamlit run PokeGame_MongoDB.py

2. Access the app in your web browser at [http://localhost:8501](http://localhost:8501).

3. Select the desired game mode: single-player or two-player.

4. Follow the instructions on the web page to play the game. Choose your Pokemon, start the battle, and watch the battle unfold!

## Dependencies

The following Python packages are required to run the Pokemon Battle Game:

- pymongo>=3.11.0
- streamlit>=1.22.0
- requests>=2.28.1
- pandas>=1.4.4

These dependencies can be installed using the `pip install -r requirements.txt` command.

## Database Setup

The game data is stored in a MongoDB database. Ensure that you have a MongoDB server running, and update the `uri` variable in the `PokeGame_MongoDB.py` file with the appropriate connection URI for your MongoDB instance.

## Contributing

Contributions to the Pokemon Battle Game are welcome! If you encounter any issues or have suggestions for improvements, please create a new issue or submit a pull request.
