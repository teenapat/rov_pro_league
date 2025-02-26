# ROV Pro League Data Pipeline

## Project Structure

```
rov_pro_league/
│── app/
│ ├── data/               # Stores JSON data
│ │ ├── matches.json      # Match-level data
│ │ ├── games.json        # Game-level data
│ │ ├── players.json      # Player statistics
│ ├── database.py         # MongoDB connection
│ ├── insert_data.py      # Inserts JSON data into MongoDB
│── config.py             # MongoDB configuration
│── .env                  # Stores MongoDB credentials
│── README.md             # Documentation
│── requirements.txt      # Requirements
```

## Overview

This project processes and stores ROV Pro League data in a MongoDB database. The data is structured into JSON files and inserted into MongoDB using Python scripts.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/teenapat/rov_pro_league.git
   cd rov_pro_league
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure environment variables:
   - Create a `.env` file with MongoDB connection details.
   ```
   MONGO_URI=mongodb+srv://your_user:your_password@your_cluster.mongodb.net/your_db
   ```

## Usage

### Inserting Data

To insert JSON data into MongoDB, run:

```bash
python app/insert_data.py
```

### Querying Data

You can interact with the database using `database.py` to perform CRUD operations on match, game, and player statistics.

## JSON Data Structure

- **matches.json**: Contains match-level information (teams, date, results).
- **games.json**: Detailed breakdown of each game within a match.
- **players.json**: Individual player statistics for each game.

## Configuration

- Modify `config.py` to update database settings if needed.

## Requirements

- Python 3.8+
- MongoDB Atlas or local MongoDB instance
- `pymongo` for database interaction

## Future Enhancements

- Implement automated data fetching
- Add analytics and visualization tools
- Optimize data indexing for faster queries

## License

This project is licensed under the MIT License.
