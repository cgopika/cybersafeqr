import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app


class MiscellaneousCrimePagesTest(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_miscellaneous_crimes_listing_page_renders(self):
        response = self.client.get('/miscellaneous-crimes')
        self.assertEqual(response.status_code, 200)

    def test_miscellaneous_category_shows_requested_crime_cards(self):
        response = self.client.get('/category/misc')
        self.assertEqual(response.status_code, 200)
        html = response.get_data(as_text=True)

        expected_titles = [
            'Tampering with Computer Source Documents',
            'Cyber Terrorism',
            'Dishonestly Receiving a Computer Resource or Communication Device',
            'Offences by Intermediaries',
            'Offences Not Attracting the IT Act'
        ]

        for title in expected_titles:
            self.assertIn(title, html)

    def test_individual_miscellaneous_crime_pages_render(self):
        crime_ids = [
            'tampering-source-documents',
            'cyber-terrorism',
            'dishonest-receiving-computer-resource',
            'offences-by-intermediaries',
            'offences-not-attracting-it-act'
        ]

        for crime_id in crime_ids:
            with self.subTest(crime_id=crime_id):
                response = self.client.get(f'/miscellaneous-crimes/{crime_id}')
                self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
