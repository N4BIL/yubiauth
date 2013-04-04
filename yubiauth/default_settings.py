#Database configuration string
DATABASE_CONFIGURATION = 'sqlite:///:memory:'

#YubiKey Validation Server URLs
YKVAL_SERVERS = [
    'https://api.yubico.com/wsapi/2.0/verify',
    'https://api2.yubico.com/wsapi/2.0/verify',
    'https://api3.yubico.com/wsapi/2.0/verify',
    'https://api4.yubico.com/wsapi/2.0/verify',
    'https://api5.yubico.com/wsapi/2.0/verify'
]

#Passlib configuration
CRYPT_CONTEXT = {
    #'schemes': ['yhsm_pbkdf2_sha1', 'sha512_crypt', 'sha256_crypt'],
    #'default': 'yhsm_pbkdf2_sha1',
    'schemes': ['sha512_crypt', 'sha256_crypt'],
    'default': 'sha256_crypt',
    'yhsm_pbkdf2_sha1__hsm': 'main',
    'yhsm_pbkdf2_sha1__key_handle': 1,
    'all__vary_rounds': 0.1,
    'sha512_crypt__min_rounds': 60000,
    'sha256_crypt__min_rounds': 80000,
    'admin__sha512_crypt__min_rounds': 120000,
    'admin__sha256_crypt__min_rounds': 160000
}

#YubiHSM, only needed if you have a YubiHSM
YHSM_DEVICES = {'main': '/dev/ttyACM0'}