import unittest
import json


class InputTests(unittest.TestCase):

    def test_valid_input(self):
        valid_json = [
            {
                "name": "Eastern Enterprise B.V.",
                "address": "Deldenerstraat 70, 7551AH Hengelo, The Netherlands"
            },
            {
                "name": "Eastern Enterprise",
                "address": "46/1 Office no 1 Ground Floor , Dada House , " +
                           "Inside dada silk mills compound, " +
                           "Udhana Main Rd, near Chhaydo Hospital, Surat, 394210, India"
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

        f = open('input.json')
        input_json = json.load(f)
        self.assertEqual(input_json, valid_json)


if __name__ == '__main__':
    unittest.main()
