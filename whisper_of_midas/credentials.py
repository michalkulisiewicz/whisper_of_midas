import keyring

class Credentials:
    def get_auth_tokens(self):
        api_key = keyring.get_password('binance', 'api_key')
        api_secret = keyring.get_password('binance', 'api_secret')
        auth_tokens = {'api_key': api_key, 'api_secret': api_secret}
        return auth_tokens

