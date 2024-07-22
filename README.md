# cfb_win_probability

Submitted assignment for Northwestern University MSDS 456 -- Sports Performance Analytics

Data extracted from the [College Football Data API](https://api.collegefootballdata.com/api/docs/?url=/api-docs.json#/)

## Setup

- create a file called `.env` to house the true CFBD API key -- the template in the env_example file should work.
- request an API key from the website's [API key section](https://collegefootballdata.com/key) and input your key in the .env file
- create and activate a virtual environment 
`py -m venv .venv`

- to activate on windows 
`./.venv/scripts/activate`

- install dependencies
`pip install -r requirements.txt`

- extract data using get_plays.py
`python get_plays.py`

- from there, the execution of the `probability_modeling.ipynb` should work as intended.

