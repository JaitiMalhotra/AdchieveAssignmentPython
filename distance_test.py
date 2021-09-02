from calculation_utils import get_all_geolocations, calculate_distance
import unittest
from dotenv import dotenv_values

config = dotenv_values(".env")


class DistanceTests(unittest.TestCase):
    """ Test module to verify address """

    def test_distance(self):
        address = [
            {
                "name": "Sherlock Holmes",
                "address": "221B Baker St., London, United Kingdom"
            }
        ]
        valid_distance = [
            {
                'Name': 'Sherlock Holmes',
                'Address': '221B Baker St., London, United Kingdom',
                'Distance': 377.22
            }
        ]

        geolocations = get_all_geolocations(address)
        calculated_distance = calculate_distance(geolocations)
        self.assertEqual(valid_distance, calculated_distance)


if __name__ == '__main__':
    unittest.main()
