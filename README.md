# Project Description

* Python script to calculate the distance from given list of addresses to Adchieve HQ, 
sorts them and stores in a CSV.

## Prerequisites

* Git
* Python3
* Virtualenv

## Setup

* Create a virtualenv using python3 `python3 -m venv env`

* Activate the virtualenv  `source env/bin/activate`

* Clone the repository `git clone git@git.easternenterprise.com:jaitimalhotra/adchieveassignment2.git`

* Install all the dependencies inside your virtualenv `pip install -r requirements.txt` 

## Usage

* Once all dependencies are installed run code by: `python calculation_utils.py --infile input.json`

* Output will be stored in the Project directory as 'distance.csv' as well shown on console.

# Input

* Input is a list of name and address of the location in this format. 
Put this input in input.json file to get output. 

`[
        {
            "name": "Eastern Enterprise B.V.",
            "address": "Deldenerstraat 70, 7551AH Hengelo, The Netherlands"
        },
        {
            "name": "Eastern Enterprise",
            "address": "46/1 Office no 1 Ground Floor , Dada House , Inside dada silk mills compound, Udhana Main Rd, near Chhaydo Hospital, Surat, 394210, India"
        },
        {
            "name": "Adchieve Rotterdam",
            "address": "Weena 505, 3013 AL Rotterdam, The Netherlands"
        },
        {
            "name": "Sherlock Holmes",
            "address": "221B Baker St., London, United Kingdom"
        },
        {
            "name": "The White House",
            "address": "1600 Pennsylvania Avenue, Washington, D.C., USA"
        },
        {
            "name": "The Empire State Building",
            "address": "350 Fifth Avenue, New York City, NY 10118"
        },
        {
            "name": "The Pope",
            "address": "Saint Martha House, 00120 Citta del Vaticano, Vatican City"
        },
        {
            "name": "Neverland",
            "address": "5225 Figueroa Mountain Road, Los Olivos, Calif. 93441, USA"
        }
    ]
`
# Test Input

* To test input run: `python -m unittest input_test.py`