from encryption_method import EncryptionMethod


class CaesarCipher(EncryptionMethod):
    """
    Class for working with Caesar Cipher.
    """

    name = "c"

    @staticmethod
    def encrypt(message):
        encrypted_message = ""

        for character in message:
            character_ascii_value = ord(character)
            character_ascii_value += 1
            encrypted_message += chr(character_ascii_value)

        return encrypted_message

    @staticmethod
    def decrypt(message):
        decrypted_message = ""

        for character in message:
            character_ascii_value = ord(character)
            character_ascii_value -= 1
            decrypted_message += chr(character_ascii_value)

        return decrypted_message
