import unittest
import json, os
import requests
os.chdir("..")
from src.migrations.clients.credentials.SpotifyCredentials import Credentials

class TestSpotifyCredentials(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        creds_json = json.loads(
        """
            {
                "access_token": "access_token_value",
                "token_type": "Bearer",
                "expires_in": 3600,
                "refresh_token": "refresh_token_value",
                "scope": "playlist-read-private playlist-read-collaborative playlist-modify-private playlist-modify-public user-read-email user-read-private"
            }
        """
        )
        self.creds = Credentials(creds_json, "auth_header_value")
    
    def test_getters(self):
        self.assertEqual(self.creds.access_token(), "access_token_value")
        self.assertEqual(self.creds.refresh_token(), "refresh_token_value")
        self.assertEqual(self.creds.auth_header(), "auth_header_value")


if __name__ == "__main__":
    unittest.main() 