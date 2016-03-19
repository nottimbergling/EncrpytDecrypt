import sys
from encryption_methods.caesar_cipher import CaesarCipher
from encryption_methods.atbash_encryption import AtbashEncryption


USAGE_ERROR_MESSAGE = "Usage: decrypter.py ENCRYPTION_METHOD ENCRYPTED_MESSAGE"
INVALID_USAGE_EXIT_CODE = -1


def main():
    """
    Controls the flow of the program.
    """
    encryption_method_to_decrypter = {CaesarCipher.name: CaesarCipher.decrypt,
                                      AtbashEncryption.name: AtbashEncryption.decrypt}

    encryption_method, encrypted_message = safe_get_command_line_arguments()

    decrypted_message = encryption_method_to_decrypter[encryption_method](encrypted_message)

    print decrypted_message


def safe_get_command_line_arguments():
    try:
        return get_command_line_arguments()
    except IndexError:
        print USAGE_ERROR_MESSAGE
        exit(INVALID_USAGE_EXIT_CODE)


def get_command_line_arguments():
    return sys.argv[1], sys.argv[2]


if "__main__" == __name__:
    main()
