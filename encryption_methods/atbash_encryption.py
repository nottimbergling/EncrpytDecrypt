from configurations.constants import LOWER_CASE_ALPHABET, UPPER_CASE_ALPHABET
from encryption_method import EncryptionMethod


class AtbashEncryption(EncryptionMethod):
    """
    Class for working with the Atbash encryption.
    """

    name = "az"

    @staticmethod
    def encrypt(message):
        encrypted_message = ""

        for character in message:
            if character in LOWER_CASE_ALPHABET:
                encrypted_character_index = (len(LOWER_CASE_ALPHABET) - 1) - LOWER_CASE_ALPHABET.index(character)
                encrypted_message += LOWER_CASE_ALPHABET[encrypted_character_index]
            elif character in UPPER_CASE_ALPHABET:
                encrypted_character_index = (len(UPPER_CASE_ALPHABET) - 1) - UPPER_CASE_ALPHABET.index(character)
                encrypted_message += UPPER_CASE_ALPHABET[encrypted_character_index]

        return encrypted_message

    @staticmethod
    def decrypt(message):
        return AtbashEncryption.encrypt(message)
